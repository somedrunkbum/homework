import sys


input_file = sys.argv[1]
output_file = sys.argv[2]

# for block in open(input_file, 'r').read(16):
#     print block

while True:
    data = open(input_file, 'r').read(16)
    print data
    if not data:
        break