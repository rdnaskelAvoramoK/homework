import sys
filename = sys.argv[1]
f = open(filename,"r")
d={}
for line in f:
	st = line.split()
	for symbols in st:
		if symbols not in d:
			d[symbols] = 1
		else:
			d[symbols] +=1
print(d)
def sortSecond(val): 
    return val[1]  
ds=list(d.items())
ds.sort(key = sortSecond)
#ds = sorted(d.items(), key=lambda x:x[1])

print(ds)
#for w in sorted(d, key=d.get, reverse=False):
	#print w, d[w]
	