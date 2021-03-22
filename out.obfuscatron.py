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
XXXX = {'__new__', '__init__', '__del__', '__repr__', '__str__',
    '__bytes__', '__format__', '__lt__', '__le__', '__eq__', '__ne__',
    '__gt__', '__ge__', '__add__', '__sub__', '__mul__', '__matmul__',
    '__truediv__', '__floordiv__', '__abs__', '__int__', '__float__',
    '__complex__', '__round__', '__trunc__', '__ceil__', '__floor__',
    '__len__', '__getitem__', '__setitem__', '__delitem__', '__iter__', 'self'
    }.union(XXXX for XXXX in dir(builtins))
XXXX = """
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
foo = "😂😂😂\"
"""


def XXXXXXXXXXX(XXXX: str):
    XXXX = brotli.compress(XXXX.encode())
    XXXX = XXXX.hex()
    return XXXX


def XXXXXXXXXXXXX(XXXX: str):
    XXXX = bytes.fromhex(XXXX)
    XXXX = brotli.decompress(XXXX)
    return XXXX.decode()


assert XXXX(XXXX(XXXX)) == XXXX


class XXXXXXXXXX:

    def XXXXXXXX(XXXX, XXXX):
        self.data = XXXX
        self.pointer = 0

    def XXXX(XXXX, XXXX):
        XXXX = self.pointer + XXXX
        XXXX = self.data[self.pointer:XXXX]
        self.pointer = XXXX
        return XXXX


class XXXXXXX(ast.NodeTransformer):

    def XXXXXXXX(XXXX, XXXX):
        ast.NodeTransformer.__init__(self)
        self.reader = XXXX
        self.name_storage = {}
        self.done = False

    def XXXXXXXXXXXX(XXXX, XXXX):
        pass

    def XXXXXXXXXX(XXXX, XXXX):
        if XXXX.id not in XXXX:
            return ast.copy_location(ast.Name(id='XXXX', ctx=ast.Load()), XXXX)
        return ast.NodeTransformer.generic_visit(self, XXXX)

    def XXXXXXXXX(XXXX, XXXX):
        if XXXX.annotation:
            XXXX = self.visit(XXXX.annotation)
        else:
            XXXX = XXXX.annotation
        return ast.copy_location(ast.arg(arg='XXXX', annotation=XXXX, ctx=
            ast.Load()), XXXX)
        return ast.NodeTransformer.generic_visit(self, XXXX)

    def XXXXXXXXXXXXXXXXX(XXXX, XXXX):
        XXXX = self.generic_visit(XXXX.args)
        return ast.copy_location(ast.FunctionDef(name='X' * len(XXXX.name),
            body=[self.visit(XXXX) for XXXX in XXXX.body], decorator_list=[
            self.visit(XXXX) for XXXX in XXXX.decorator_list], args=XXXX), XXXX
            )
        return XXXX

    def XXXXXXXXXXXXXX(XXXX, XXXX):
        print(dir(XXXX))
        return ast.copy_location(ast.ClassDef(name='X' * len(XXXX.name),
            bases=[self.visit(XXXX) for XXXX in XXXX.bases], body=[self.
            visit(XXXX) for XXXX in XXXX.body], decorator_list=[self.visit(
            XXXX) for XXXX in XXXX.decorator_list], keywords=[self.visit(
            XXXX) for XXXX in XXXX.keywords]), XXXX)

    def XXXXXXXXXXXX(XXXX, XXXX):
        XXXX = [getattr(XXXX, 'id', getattr(XXXX, 'name', '')) for XXXX in
            XXXX.names]
        XXXX.update(XXXX)
        for XXXX in XXXX.names:
            self.visit(XXXX)
        return ast.NodeTransformer.generic_visit(self, XXXX)

    def XXXXXXXXXXXXXXXX(XXXX, XXXX):
        XXXX = [getattr(XXXX, 'id', getattr(XXXX, 'name', '')) for XXXX in
            XXXX.names]
        XXXX.update(XXXX)
        return XXXX

    def XXXXXXXXXXXXXXXXXXXXXXXXXXXX(XXXX, XXXX):
        XXXX = None
        if isinstance(XXXX, (ast.Import, ast.ImportFrom)):
            XXXX.update(XXXX.names)
        elif not self.done:
            if isinstance(XXXX, (ast.FunctionDef, ast.ClassDef)):
                XXXX = XXXX.name
            elif isinstance(XXXX, ast.Name):
                XXXX = XXXX.id
            if XXXX and XXXX not in XXXX:
                print(XXXX)
                if XXXX in self.name_storage:
                    XXXX = self.name_storage[XXXX]
                else:
                    XXXX = self.reader.read(len(XXXX))
                    XXXX = '_' + XXXX
                    if len(XXXX) < len(XXXX):
                        XXXX += 'd____b'
                        self.done = True
                    self.name_storage[XXXX] = XXXX
                    return ast.copy_location(ast.Name(id=XXXX, ctx=ast.Load
                        ()), XXXX)
        if XXXX:
            print(':(', XXXX)
        return super().generic_visit(XXXX)


def XXXX(XXXX):
    XXXX, XXXX = XXXX[0], XXXX[1] == 'encode'
    XXXX = XXXX(XXXX(XXXX))
    XXXX = ast.parse(open(XXXX).read())
    XXXX = XXXX(XXXX).visit(XXXX)
    with open('out.obfuscatron.py', 'w') as XXXX:
        XXXX.write(astor.to_source(XXXX))


XXXX(['main.py', 'encode'])
