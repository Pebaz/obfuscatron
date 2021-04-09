import sys
from os import pathsep
from typing import List


class _0b0(object):

    def __init__(self, _1803):
        self.name = _1803
        self.foo = 'asdf'
        self.a1 = sys.argv
        self.a2 = self.a1.clear
        _1323303d____b = 100
        self.what = _1323303d____b
        self.asdf = [1, 2, 3]
        self.asdf[-1] = _1323303d____b
        with open('foo') as _1crm:
            print(_1crm.read())


_o3wened = List[str]


def _i239(_w559z: _o3wened):
    _as2qecpyl = 0
    for _v4e9vweut in _w559z:
        _as2qecpyl += 1
        print(_v4e9vweut)
    return _as2qecpyl


_7e6x69 = _i239(pathsep.join(sys.path).split(pathsep))
print(_7e6x69)
print(pathsep)
print(sys)
