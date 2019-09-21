import sys, re
filename = sys.argv[1]
f = open(filename,'r')

def fun1(text):
	#разбите текста по словам и сздание словаря d
	list(map(lambda y: d.extend(y),list(map(lambda x: re.split('[^\w\']',x.lower()),text))))
	#удаление пустых элементов
	r=list(filter(lambda z: z!="",d))
	#подсчёт элементов и генерация словаря с словами и кол-м повторений в тексте
	d_t=dict((a,r.count(a)) for a in r if a not in dict_t)
	return d_t
d=[]
dict_t={}
d=fun1(f)
#print(d)
for key, value in d.items():
 	print(key,":",value)