import sys
from os import pathsep


def show(items):
    the_count = 0
    for each_name in items:
        the_count += 1
        print(each_name)
    return the_count


result = show(pathsep.join(sys.path).split(pathsep))

print(result)
print(pathsep)
print(sys)
