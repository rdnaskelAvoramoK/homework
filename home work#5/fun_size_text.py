import sys, random
inp_filename1 = sys.argv[1]
inp_filename2 = sys.argv[2]
def small(l):
	return l.lower()
def big(l):
	return l.upper()
fr1 = open(inp_filename1,"r")
l1 = list(map(small,fr1))
fr2 = open(inp_filename2,"r")
l2 = list(map(big,fr2))
print("small text")
list(map(lambda line: print(line),l1))
print("\n\nbig text")
list(map(lambda line: print(line),l2))