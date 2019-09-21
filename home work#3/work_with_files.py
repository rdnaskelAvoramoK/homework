import sys
filename = sys.argv[1]
f = open(filename,'r')
fw = open('t.txt','w')
for line in f:
	fw.write(line)
	print(line)
f.close()