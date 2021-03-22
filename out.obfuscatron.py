import sys
from os import pathsep
from typing import List


class _1bc(object):

    def __init__(self, _e000):
        self.name = _e000
        self.foo = 'asdf'
        self.a1 = sys.argv
        self.a2 = self.a1.clear
        _02c0eec86d77b1da1 = 100
        self.what = _02c0eec86d77b1da1
        self.asdf = [1, 2, 3]
        self.asdf[-1] = _02c0eec86d77b1da1
        with open('foo') as _0bbf:
            print(_0bbf.read())


_c7ec12a = List[str]


def _9d4f(_02ab3: _c7ec12a):
    _6837a06d3 = 0
    for _f68205916 in _02ab3:
        _6837a06d3 += 1
        print(_f68205916)
    return _6837a06d3


_604114 = _9d4f(pathsep.join(sys.path).split(pathsep))
print(_604114)
print(pathsep)
print(sys)
