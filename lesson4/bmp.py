import sys
import struct


import_file_name = sys.argv[1]
export_file_name = sys.argv[2]

input_file = open(import_file_name, 'rb')
data = input_file.read()
file_header = struct.unpack("<ccihhi", data[:14])
headers_size = file_header[5]
pixel_size = len(data) - headers_size
print("file_header is {}".format(file_header))
print("INFO: file size from header is {}".format(file_header[2]))
print("INFO: file size in memory is {}".format(len(data)))
print("INFO: headers size is {}".format(headers_size))

changed_data = data[:headers_size] + pixel_size*'\xff'
open(export_file_name, "wb").write(changed_data)