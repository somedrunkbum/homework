import sys


def num_sum(*args):
    n = 0
    for i in args:
        n += sum(i)
    return n

print num_sum(map(int, sys.argv[1:]))
