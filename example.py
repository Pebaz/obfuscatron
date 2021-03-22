import sys
from os import pathsep
from typing import List

class Foo(object):
    def __init__(self, name):
        self.name = name

FooList = List[str]

def show(items: FooList):
    the_count = 0
    for each_name in items:
        the_count += 1
        print(each_name)
    return the_count


result = show(pathsep.join(sys.path).split(pathsep))

print(result)
print(pathsep)
print(sys)
