import sys, builtins, ast, random, string
from pathlib import Path
import astor, brotli


IGNORE_NAMES = {
    '__new__', '__init__', '__del__', '__repr__', '__str__', '__bytes__',
    '__format__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__',
    '__add__', '__sub__', '__mul__', '__matmul__', '__truediv__',
    '__floordiv__', '__abs__', '__int__', '__float__', '__complex__',
    '__round__', '__trunc__', '__ceil__', '__floor__', '__len__', '__getitem__',
    '__setitem__', '__delitem__', '__iter__', 'self'
}.union(i for i in dir(builtins))


def get_random_string(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.SystemRandom().choice(letters) for _ in range(length))


def obfuscatron(data: bytes):
    compressed = brotli.compress(data)
    encoded = compressed.hex()
    return encoded


def deobfuscatron(data: str):
    decoded = bytes.fromhex(data)
    decompressed = brotli.decompress(decoded)
    return decompressed


class DataReader:
    def __init__(self, data):
        self.data = data
        self.pointer = 0
    
    def read(self, chunk_size):
        end = self.pointer + chunk_size
        result = self.data[self.pointer:end]
        self.pointer = end  # min(end, len(self.data) - 1)
        return result
    
    def empty(self):
        return self.pointer >= len(self.data) - 1


class Encoder(ast.NodeTransformer):
    def __init__(self, reader):
        ast.NodeTransformer.__init__(self)
        self.reader = reader
        self.name_storage = {}
        self.IGNORE_NAMES = {*IGNORE_NAMES}
        self.done = False
    
    def get_new_name(self, node_name):
        if node_name and node_name not in self.IGNORE_NAMES:

            if node_name in self.name_storage:
                new_name = self.name_storage[node_name]
            
            else:
                data = self.reader.read(len(node_name))
                new_name = '_' + data

                if not data:
                    if not self.done:
                        new_name += 'd____b'
                    else:
                        new_name += get_random_string(len(node_name))
                    self.done = True

                elif len(data) < len(node_name):
                    new_name += 'd____b'
                    self.done = True

                self.name_storage[node_name] = new_name

            return new_name
        return node_name


    def visit_Assign(self, node):
        return ast.copy_location(
            ast.Assign(
                value=self.visit(node.value),
                targets=[self.visit(i) for i in node.targets],
                ctx=ast.Load()
            ),
            node
        )
    
    # TODO(pebaz): Get attributes working properly
    # def visit_Attribute(self, node):
    #     return ast.copy_location(
    #         ast.Attribute(
    #             value=self.visit(node.value),
    #             attr=self.visit(node.attr),
    #             # attr=node.attr,
    #             ctx=ast.Load()
    #         ),
    #         node
    #     )

    def visit_Name(self, node):
        if node.id not in self.IGNORE_NAMES:
            return ast.copy_location(
                ast.Name(
                    id=self.get_new_name(node.id),
                    ctx=ast.Load()
                ),
                node
            )
        return ast.NodeTransformer.generic_visit(self, node)
        
    
    def visit_arg(self, node):
        if node.annotation:
            annotation = self.visit(node.annotation)
        else:
            annotation = node.annotation

        return ast.copy_location(
            ast.arg(
                arg=self.get_new_name(node.arg),
                annotation=annotation,
                ctx=ast.Load()
            ),
            node
        )

    def visit_FunctionDef(self, node):
        return ast.copy_location(
            ast.FunctionDef(
                name=self.get_new_name(node.name),
                body=[self.visit(i) for i in node.body],
                decorator_list=[self.visit(i) for i in node.decorator_list],
                args=self.generic_visit(node.args),
            ),
            node
        )

    def visit_ClassDef(self, node):
        return ast.copy_location(
            ast.ClassDef(
                name=self.get_new_name(node.name),
                bases=[self.visit(i) for i in node.bases],
                body=[self.visit(i) for i in node.body],
                decorator_list=[self.visit(i) for i in node.decorator_list],
                keywords=[self.visit(i) for i in node.keywords]
            ),
            node
        )
        
    
    def visit_Import(self, node):
        names = [getattr(n, 'id', getattr(n, 'name', '')) for n in node.names]
        self.IGNORE_NAMES.update(names)
        for inner in node.names:
            self.visit(inner)
        return ast.NodeTransformer.generic_visit(self, node)
    
    def visit_ImportFrom(self, node):
        names = [getattr(n, 'id', getattr(n, 'name', '')) for n in node.names]
        self.IGNORE_NAMES.update(names)
        return node


class Decoder(ast.NodeTransformer):
    def __init__(self):
        ast.NodeTransformer.__init__(self)
        self.name_storage = {}
        self.IGNORE_NAMES = {*IGNORE_NAMES}
        self.done = False

    def visit_Assign(self, node):
        return ast.copy_location(
            ast.Assign(
                value=self.visit(node.value),
                targets=[self.visit(i) for i in node.targets],
                ctx=ast.Load()
            ),
            node
        )

    def visit_Name(self, node):
        if node.id not in self.IGNORE_NAMES:
            self.name_storage[node.id] = 0
        return ast.NodeTransformer.generic_visit(self, node)
    
    def visit_arg(self, node):
        if node.arg not in self.IGNORE_NAMES:
            self.name_storage[node.arg] = 0
        return ast.NodeTransformer.generic_visit(self, node)

    def visit_FunctionDef(self, node):
        if node.name not in self.IGNORE_NAMES:
            self.name_storage[node.name] = 0

        [self.visit(i) for i in node.decorator_list]
        [self.visit(i) for i in node.body]
        self.generic_visit(node.args)
        return ast.NodeTransformer.generic_visit(self, node)

    def visit_ClassDef(self, node):
        if node.name not in self.IGNORE_NAMES:
            self.name_storage[node.name] = 0
        [self.visit(i) for i in node.bases]
        [self.visit(i) for i in node.body]
        [self.visit(i) for i in node.decorator_list]
        [self.visit(i) for i in node.keywords]
        return ast.NodeTransformer.generic_visit(self, node)
    
    def visit_Import(self, node):
        names = [getattr(n, 'id', getattr(n, 'name', '')) for n in node.names]
        self.IGNORE_NAMES.update(names)
        for inner in node.names:
            self.visit(inner)
        return ast.NodeTransformer.generic_visit(self, node)
    
    def visit_ImportFrom(self, node):
        names = [getattr(n, 'id', getattr(n, 'name', '')) for n in node.names]
        self.IGNORE_NAMES.update(names)
        return node


def main(args=None):
    args = args or sys.argv[1:]

    try:
        py_file = args[0]
        encode = args[1] == 'encode'
        data_file = args[2]
        out_file = args[3]
    except (ValueError, IndexError):
        try:
            py_file = args[0]
            encode = args[1] == 'encode'
            data_file = args[2]

            assert encode in {'encode', 'decode'}
        except (ValueError, IndexError, AssertionError):
            print(
                'obfuscatron - store data in Python source files pretending to '
                'be obfuscated\n'
                'Usage:\n'
                '  obfuscatron FILE.py encode DATAFILE OUTFILE\n'
                '  obfuscatron OUTFILE.py decode DATAFILE'
            )
            return

    if encode:
        input_data = Path(data_file).read_bytes()
        reader = DataReader(obfuscatron(input_data))
        tree = ast.parse(open(py_file).read())
        encoder = Encoder(reader)
        obfuscated = encoder.visit(tree)

        # Any data left in reader?
        assert reader.empty(), (
            f'Not enough storage space in file! '
            f'Need {len(reader.data)} bytes but file storage capacity is '
            f'{reader.pointer} bytes'
        )

        with open(out_file, 'w') as file:
            file.write(astor.to_source(obfuscated))
    else:
        tree = ast.parse(open(py_file).read())
        decoder = Decoder()
        tree = decoder.visit(tree)
        buffer = ''

        for x in decoder.name_storage:
            buffer += x[1:].replace('d____b', '')

            if 'd____b' in x:
                break

        print(buffer)

        output_data = deobfuscatron(buffer)

        with open(data_file, 'wb') as file:
            file.write(output_data)

# TODO(pebaz): setup.py
# TODO(pebaz): Upload to PyPI


if __name__ == '__main__':
    main(sys.argv[1:])
