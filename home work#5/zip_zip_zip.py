print(" Hello! This is my Zip.\n"
"You can create any type of data except dictionaries. \n"
"Zip will record data sequentially for each data item.\n\n")

names_data=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
 'o','p','q','r','s','t','u','v','w','x','y','z']

def siporato(text):
	return (int(x) if x.isdigit() else x for x in text.split(','))

def create_a_list(text):
	return list(siporato(text))

def create_a_tuple(text):
	return tuple(siporato(text))

def create_a_set(text):
	return set(siporato(text))

def print_args(args):
	for el in range(len(args)):
		print(names_data[el],'=',args[el],'\n',type(args[el]))

def shortest_sequence_range(args):
	return range(len(sorted(args, key=len)[0]))

def extraction(i,args):
	l=[]
	for el in args:
		l.extend(list(valure for item, valure in enumerate(el) if item==i))
	return tuple(l)

Array={
1:create_a_list,
2:create_a_tuple,
3:create_a_set
}

args=[]
my_zip=[]

while True:
	for n_arg in names_data:
		arg=n_arg
		arg=input('Enter data, if it is not a string - then through \",\"\n'
'if you want to exit input \"exit\"\n'+str(n_arg)+"=")
		if arg == "exit":
			break
		type_arg=int(input('Select data type:\n'
			"1.list\n"
			"2.tuple\n"
			"3.set (you will lose duplicate data)\n"
			"4.strig\n___"))
		if type_arg !=4:
			args.append(Array[type_arg](arg))
		else:
			args.append(arg)
		print_offer=input('\nDo you want to see all the data? (y/n) __')
		if print_offer=="y":
			print_args(args)
	break		

my_zip=(extraction(i,args) for i in shortest_sequence_range(args))

for el in my_zip:
	print(el)
