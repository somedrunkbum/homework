import sys


def string_format(line):
    for i in line:
        if i % 2 == 0:
            print "An even number: %s" % (i)
        else:
            print "An odd number: %s" % (i)
    return

line = map(int, sys.argv[1:])
string_format(line)