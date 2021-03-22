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
_8b04800a6e616d65203d20456103 = """
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


def obfuscatron(data: str):
    _8b04807274680a72616469757303 = _8b0280203d2033393003.compress(
        _8b01803030303003.encode())
    _0b0380300a746572726503 = _8b04807274680a72616469757303.hex()
    return _0b0380300a746572726503


def deobfuscatron(data: str):
    _0b038073747269616c2003 = bytes.fromhex(_8b01803030303003)
    _8b05803d20547275650a666f6f203d03 = _8b0280203d2033393003.decompress(
        _0b038073747269616c2003)
    return _8b05803d20547275650a666f6f203d03.decode()


assert _8b07802022f09f9882220a0a6e616d65203d2003(
    _0b05804d6172730a72616469757303(_8b04800a6e616d65203d20456103)
    ) == _8b04800a6e616d65203d20456103


class DataReader:

    def __init__(self, data):
        self.data = _8b01803030303003
        self.pointer = 0

    def read(self, chunk_size):
        _0b0180203d2003 = self.pointer + _8b04803132333439323832333803
        _8b0280320a7465727203 = self.data[self.pointer:_0b0180203d2003]
        self.pointer = _0b0180203d2003
        return _8b0280320a7465727203


class Encoder(_0b018065737403.NodeTransformer):

    def __init__(self, reader):
        _0b018065737403.NodeTransformer.__init__(self)
        self.reader = _8b02807269616c203d03
        self.builtin_names = set(dir(_8b038020547275650a666f03))
        self.builtin_names.add('self')
        self.name_storage = {}
        self.done = False

    def visit_Name(self, node):
        if _8b01806f203d2003.id in self.builtin_names:
            return _8b01806f203d2003
        elif _8b01806f203d2003.id in self.name_storage:
            _8b068022f09f9882220a0a6e616d65203d03 = self.name_storage[
                _8b01806f203d2003.id]
            return _0b018065737403.copy_location(_0b018065737403.Name(id=
                _8b068022f09f9882220a0a6e616d65203d03, ctx=_0b018065737403.
                Load()), _8b01806f203d2003)
        elif self.done:
            return _8b01806f203d2003
        _8b01803030303003 = self.reader.read(len(_8b01806f203d2003.id))
        if not _8b01803030303003:
            _1b0700f82500a29088681b = 'd_____b'
            self.done = True
        _8b04800a726164697573203d2003 = _0b05804d6172730a72616469757303(
            _8b01803030303003)
        if len(_8b01803030303003) < len(_8b01806f203d2003.id):
            _1b0700f82500a29088681b = ('_' + _8b04800a726164697573203d2003 +
                'd_____b')
        else:
            _1b0700f82500a29088681b = '_' + _8b04800a726164697573203d2003
        self.name_storage[_8b01806f203d2003.id] = _1b0700f82500a29088681b
        return _0b018065737403.copy_location(_0b018065737403.Name(id=
            _1b0700f82500a29088681b, ctx=_0b018065737403.Load()),
            _8b01806f203d2003)


def main(args):
    _8b0380343330303031323303, _8b028032330a74657203 = _8b01807265737403[0
        ], _8b01807265737403[1] == 'encode'
    _8b02807269616c203d03 = _8b04807269616c203d2046616c03(
        _8b04800a6e616d65203d20456103)
    _8b018073650a6603 = _0b018065737403.parse(open(
        _8b0380343330303031323303).read())
    _8b018073650a6603 = _8b04806f6f203d2022f09f988203(_8b02807269616c203d03
        ).visit(_8b018073650a6603)
    with open('out.obfuscatron.py', 'w') as _8b0480f09f9882f09f9882220a03:
        _8b0480f09f9882f09f9882220a03.write(_3bd_____b.to_source(
            _8b018073650a6603))


main(['main.py', 'encode'])
quit()
source = """
something = 1
something_else = 2 ** something
def add(a: int, b: int) -> int:
    if not all((isinstance(a, int), isinstance(b, int))):
        raise TypeError('Arguments must be int')
    return a + b
"""
_8b018073650a6603 = _0b018065737403.parse(source)
_8b038020547275650a666f03 = set(dir(_8b038020547275650a666f03))
_8b01803030303003 = {}
encrypt = True


class RewriteName(_0b018065737403.NodeTransformer):

    def visit_Name(self, node):
        global data, encrypt
        if _8b01806f203d2003.id in _8b038020547275650a666f03:
            return _8b01806f203d2003
        if encrypt:
            _1b0700f82500a29088681b = _8b01803030303003.setdefault(
                _8b01806f203d2003.id, _8b01806f203d2003.id.upper())
        else:
            _1b0700f82500a29088681b = _8b01803030303003.setdefault(
                _8b01806f203d2003.id, _8b01806f203d2003.id.lower())
        return _0b018065737403.copy_location(_0b018065737403.Name(id=
            _1b0700f82500a29088681b, ctx=_0b018065737403.Load()),
            _8b01806f203d2003)


_8b018073650a6603 = RewriteName().visit(_8b018073650a6603)
print('Before:', textwrap.indent(source, ' |  '))
print('After:\n' + textwrap.indent(_3bd_____b.to_source(_8b018073650a6603),
    ' |  '))
print(_8b01803030303003)
print('Data Storage Capacity:', sum(len(i) for i in _8b01803030303003))
encrypt = False
_8b018073650a6603 = RewriteName().visit(_8b018073650a6603)
print('After:\n' + textwrap.indent(_3bd_____b.to_source(_8b018073650a6603),
    ' |  '))
print(_8b01803030303003)
