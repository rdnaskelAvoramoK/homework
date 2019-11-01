import sys

filename = sys.argv[1]
file_handler = open(filename,'r')

for line in file_handler:
    print(line)

file_handler.close()