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
        with open('foo') as _d____b:
            print(_d____b.read())


_d____b = List[str]


def _d____b(_d____b: _d____b):
    _d____b = 0
    for _d____b in _d____b:
        _d____b += 1
        print(_d____b)
    return _d____b


_d____b = _d____b(pathsep.join(sys.path).split(pathsep))
print(_d____b)
print(pathsep)
print(sys)
