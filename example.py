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


super_long_variable_name = 3
super_long_variable_name2 = 4
super_long_variable_name3 = 5
super_long_variable_name4 = 6
super_long_variable_name5 = 7
super_long_variable_name6 = 8
super_long_variable_name7 = 9
super_long_variable_name8 = 10
super_long_variable_name9 = 11
super_long_variable_name10 = 12
super_long_variable_name11 = 13
super_long_variable_name12 = 14


print(
    super_long_variable_name,
    super_long_variable_name2,
    super_long_variable_name3,
    super_long_variable_name4,
    super_long_variable_name5,
    super_long_variable_name6,
    super_long_variable_name7,
    super_long_variable_name8,
    super_long_variable_name9,
    super_long_variable_name10,
    super_long_variable_name11,
    super_long_variable_name12
)

_a_super_long_variable_name = 3
_a_super_long_variable_name2 = 4
_a_super_long_variable_name3 = 5
_a_super_long_variable_name4 = 6
_a_super_long_variable_name5 = 7
_a_super_long_variable_name6 = 8
_a_super_long_variable_name7 = 9
_a_super_long_variable_name8 = 10
_a_super_long_variable_name9 = 11
_a_super_long_variable_name10 = 12
_a_super_long_variable_name11 = 13
_a_super_long_variable_name12 = 14

_b_super_long_variable_name = 3
_b_super_long_variable_name2 = 4
_b_super_long_variable_name3 = 5
_b_super_long_variable_name4 = 6
_b_super_long_variable_name5 = 7
_b_super_long_variable_name6 = 8
_b_super_long_variable_name7 = 9
_b_super_long_variable_name8 = 10
_b_super_long_variable_name9 = 11
_b_super_long_variable_name10 = 12
_b_super_long_variable_name11 = 13
_b_super_long_variable_name12 = 14

_c_super_long_variable_name = 3
_c_super_long_variable_name2 = 4
_c_super_long_variable_name3 = 5
_c_super_long_variable_name4 = 6
_c_super_long_variable_name5 = 7
_c_super_long_variable_name6 = 8
_c_super_long_variable_name7 = 9
_c_super_long_variable_name8 = 10
_c_super_long_variable_name9 = 11
_c_super_long_variable_name10 = 12
_c_super_long_variable_name11 = 13
_c_super_long_variable_name12 = 14

_d_super_long_variable_name = 3
_d_super_long_variable_name2 = 4
_d_super_long_variable_name3 = 5
_d_super_long_variable_name4 = 6
_d_super_long_variable_name5 = 7
_d_super_long_variable_name6 = 8
_d_super_long_variable_name7 = 9
_d_super_long_variable_name8 = 10
_d_super_long_variable_name9 = 11
_d_super_long_variable_name10 = 12
_d_super_long_variable_name11 = 13
_d_super_long_variable_name12 = 14
