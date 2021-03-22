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


def _02ab(_05916: _c7ec12a):
    _39d4f6837 = 0
    for _a06d3f682 in _05916:
        _39d4f6837 += 1
        print(_a06d3f682)
    return _39d4f6837


_604114 = _02ab(pathsep.join(sys.path).split(pathsep))
print(_604114)
print(pathsep)
print(sys)
