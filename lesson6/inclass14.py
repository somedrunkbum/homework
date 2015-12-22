import sys


filepath = sys.argv[1]
pattern = sys.argv[2]

for line in open(filepath):
    if pattern.lower() in line:
        print line
