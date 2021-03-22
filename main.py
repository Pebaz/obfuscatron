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
        self.builtin_names = set(dir(builtins))
        self.builtin_names.add('self')
        self.name_storage = {}
        self.done = False

    def visit_Name(self, node):
        if node.id in self.builtin_names:
            return node

        elif node.id in self.name_storage:
            precomputed = self.name_storage[node.id]
            return ast.copy_location(
                ast.Name(id=precomputed, ctx=ast.Load()),
                node
            )
        
        elif self.done:
            return node

        data = self.reader.read(len(node.id))

        if not data:
            new_name = 'd_____b'
            self.done = True

        obfuscated = obfuscatron(data)

        if len(data) < len(node.id):
            new_name = '_' + obfuscated + 'd_____b'
        else:
            new_name = '_' + obfuscated

        self.name_storage[node.id] = new_name

        return ast.copy_location(ast.Name(id=new_name, ctx=ast.Load()), node)



def main(args):
    filename, encode = args[0], args[1] == 'encode'

    reader = DataReader(input_data)

    tree = ast.parse(open(filename).read())
    tree = Encoder(reader).visit(tree)

    with open('out.obfuscatron.py', 'w') as file:
        file.write(astor.to_source(tree))


main(['main.py', 'encode'])
quit()


source = '''
something = 1
something_else = 2 ** something
def add(a: int, b: int) -> int:
    if not all((isinstance(a, int), isinstance(b, int))):
        raise TypeError('Arguments must be int')
    return a + b
'''

tree = ast.parse(source)

builtins = set(dir(builtins))
data = {}
encrypt = True

class RewriteName(ast.NodeTransformer):
    def visit_Name(self, node):
        global data, encrypt

        if node.id in builtins:
            return node

        if encrypt:
            new_name = data.setdefault(node.id, node.id.upper())
        else:
            new_name = data.setdefault(node.id, node.id.lower())

        return ast.copy_location(ast.Name(id=new_name, ctx=ast.Load()), node)

tree = RewriteName().visit(tree)

print('Before:', textwrap.indent(source, ' |  '))
print('After:\n' + textwrap.indent(astor.to_source(tree), ' |  '))

print(data)
print('Data Storage Capacity:', sum(len(i) for i in data))

encrypt = False
tree = RewriteName().visit(tree)
print('After:\n' + textwrap.indent(astor.to_source(tree), ' |  '))
print(data)
