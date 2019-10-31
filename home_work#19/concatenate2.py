import sys

for filename in sys.argv:
    file_handler = open(filename,'r')
    for line in file_handler:
        print(line)

    file_handler.close()