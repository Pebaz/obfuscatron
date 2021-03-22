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


# compressed = brotli.compress(input_data.encode())
# encoded = compressed.hex()

# print('    Normal:', len(input_data.encode()))
# print('Compressed:', len(compressed))
# print('Encoded:', len(encoded), encoded)

# decoded = bytes.fromhex(encoded)
# print('Decoded:', len(encoded), decoded)
# decompressed = brotli.decompress(decoded)
# print('Decompressed:', len(decompressed))
# normal = decompressed.decode()
# print('    Normal:', len(normal), normal)

# print('Successful:', normal == input_data)

assert deobfuscatron(obfuscatron(input_data)) == input_data

print(obfuscatron(input_data))
print(deobfuscatron(obfuscatron(input_data)))

quit()

compressed = brotli.compress(input_data.encode())

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
