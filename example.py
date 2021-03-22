import sys
from os import pathsep
from typing import List

class Foo(object):
    def __init__(self, name):
        self.name = name
        self.foo = 'asdf'

        self.a1 = sys.argv
        self.a2 = self.a1.clear

        what_in_the_world = 100
        self.what = what_in_the_world

        self.asdf = [1, 2, 3]
        self.asdf[-1] = what_in_the_world

        with open('foo') as file:
            print(file.read())

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
