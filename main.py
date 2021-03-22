"""
Encryption Plan:
1. Take in an amount of input text, brotli compress it and convert it to base64
2. For each name in a given Python file, store an amount of text from input
3. If run out of space or end of input data is encountered, write magic byte

Decryption Plan:
1. Take in a given Python file and scrape out all the names
2. For each name, base64 decode it and then brotli decompress it
3. If magic byte is encountered, halt program
"""

import builtins, ast, textwrap, base64
from urllib.parse import quote_plus
import astor, brotli


IGNORE_NAMES = {
    '__new__', '__init__', '__del__', '__repr__', '__str__', '__bytes__',
    '__format__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__',
    '__add__', '__sub__', '__mul__', '__matmul__', '__truediv__',
    '__floordiv__', '__abs__', '__int__', '__float__', '__complex__',
    '__round__', '__trunc__', '__ceil__', '__floor__', '__len__', '__getitem__',
    '__setitem__', '__delitem__', '__iter__', 'self'
}.union(i for i in dir(builtins))




input_data = '''
name = Earth
radius = 39000000
terrestrial = True
foo = "😂"

name = Mars
radius = 12349282382
terrestrial = True
foo = "😂"

name = Jupiter
radius = 4300012323
terrestrial = False
foo = "😂😂😂"
'''

def obfuscatron(data: str):
    compressed = brotli.compress(data.encode())
    encoded = compressed.hex()
    return encoded


def deobfuscatron(data: str):
    decoded = bytes.fromhex(data)
    decompressed = brotli.decompress(decoded)
    return decompressed.decode()


assert deobfuscatron(obfuscatron(input_data)) == input_data


# Treat bytes.fromhex() error as end of stream. Use underscores to mark this

class DataReader:
    def __init__(self, data):
        self.data = data
        self.pointer = 0
    
    def read(self, chunk_size):
        end = self.pointer + chunk_size
        result = self.data[self.pointer:end]
        self.pointer = end
        return result


class Encoder(ast.NodeTransformer):
    def __init__(self, reader):
        ast.NodeTransformer.__init__(self)
        self.reader = reader
        self.name_storage = {}
        self.done = False
    
    def get_new_name(self, node_name):
        return 'X' * len(node_name)

    def visit_Assign(self, node):
        return ast.copy_location(
            ast.Assign(
                value=self.visit(node.value),
                targets=[self.visit(i) for i in node.targets],
                ctx=ast.Load()
            ),
            node
        )
    
    def visit_Attribute(self, node):
        # import ipdb; ipdb.set_trace()
        return node
        return ast.copy_location(
            ast.Assign(
                value=self.visit(node.value),
                targets=[self.visit(i) for i in node.targets],
                ctx=ast.Load()
            ),
            node
        )

    def visit_Name(self, node):
        if node.id not in IGNORE_NAMES:
            return ast.copy_location(
                ast.Name(id=self.get_new_name(node.id), ctx=ast.Load()),
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
        
        return ast.NodeTransformer.generic_visit(self, node)

    def visit_FunctionDef(self, node):
        # import ipdb; ipdb.set_trace()

        args = self.generic_visit(node.args)
        # try:
        #     args = self.visit(node.args)
        # except AttributeError:
        #     args = node.args
        return ast.copy_location(
            ast.FunctionDef(
                name=self.get_new_name(node.name),
                body=[self.visit(i) for i in node.body],
                decorator_list=[self.visit(i) for i in node.decorator_list],
                args=args,
            ),
            node
        )
        return node

    def visit_ClassDef(self, node):
        print(dir(node))
        # return ast.NodeTransformer.generic_visit(self, node)
        #return node

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
        IGNORE_NAMES.update(names)
        for inner in node.names:
            self.visit(inner)
        return ast.NodeTransformer.generic_visit(self, node)
    
    def visit_ImportFrom(self, node):
        names = [getattr(n, 'id', getattr(n, 'name', '')) for n in node.names]
        IGNORE_NAMES.update(names)
        return node

    # def visit_Name(self, node):
    #     if node.id in self.builtin_names:
    #         return node

    #     elif node.id in self.name_storage:
    #         precomputed = self.name_storage[node.id]
    #         return ast.copy_location(
    #             ast.Name(id=precomputed, ctx=ast.Load()),
    #             node
    #         )
        
    #     elif self.done:
    #         return node

    #     data = self.reader.read(len(node.id))

    #     if not data:
    #         new_name = 'd_____b'
    #         self.done = True

    #     obfuscated = obfuscatron(data)

    #     if len(data) < len(node.id):
    #         new_name = '_' + obfuscated + 'd_____b'
    #     else:
    #         new_name = '_' + obfuscated

    #     self.name_storage[node.id] = new_name

    #     return ast.copy_location(ast.Name(id=new_name, ctx=ast.Load()), node)
    
    def asdfasdfasfdasdfasdfasdfasdf(self, node):
        node_name = None

        if isinstance(node, (ast.Import, ast.ImportFrom)):
            IGNORE_NAMES.update(node.names)

        elif not self.done:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                node_name = node.name
            elif isinstance(node, ast.Name):
                node_name = node.id
            if node_name and node_name not in IGNORE_NAMES:
                print(node_name)

                if node_name in self.name_storage:
                    new_name = self.name_storage[node_name]
                
                else:
                    data = self.reader.read(len(node_name))
                    new_name = '_' + data

                    if len(data) < len(node_name):
                        new_name += 'd____b'
                        self.done = True

                    self.name_storage[node_name] = new_name

                    return ast.copy_location(
                        ast.Name(id=new_name, ctx=ast.Load()),
                        node
                    )

        if node_name:
            print(':(', node_name)
        return super().generic_visit(node)


def main(args):
    filename, encode = args[0], args[1] == 'encode'

    reader = DataReader(obfuscatron(input_data))

    tree = ast.parse(open(filename).read())
    tree = Encoder(reader).visit(tree)

    with open('out.obfuscatron.py', 'w') as file:
        file.write(astor.to_source(tree))


main(['example.py', 'encode'])

