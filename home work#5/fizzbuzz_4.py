import sys, random
inp_filename = sys.argv[1]
out_filename = sys.argv[2]
fr = open(inp_filename,"r")
fw = open(out_filename,"w")
print("""
Задача fizz-buzz:\n
У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz.
До третьего необходимо досчитать от единицы. Считая, надо выводить число. 
Если число кратно fizz - надо выводить F вместо числа. Если число кратно buzz - надо выводить B вместо числа.
Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.\n\n""")
inp_cell1=input("""
1. Продолжить работать с текущими файлами
2. Хочешь прочитать другой файл с числами
3. Хочешь сгенерировать файл
4. Работать без участия файла\n___""")

def rand_n(name):
	t = open(name,'w')
	qt_l = int(input("Введи количество сторк____",))
	qty = int(input("Введи наибольшее число в диапазоне ____",))
	for x in range(1,qt_l+1):
		last_n = random.randint(10,qty)
		fizz = random.randint(1,last_n//4)
		buzz = random.randint(1,last_n//3)
		if fizz == buzz:
			buzz = random.randint(1,last_n//5)
		line = str(fizz) + " " + str(buzz) + " " + str(last_n) + "\n"
		print(line)
		t.write(line) 
	t.close()
# вывод содержания файла ввода
def print_inp(info):
	print("\nСодержание файла ",inp_filename,":\n")
	for line in info:
		print(line)
# ручной ввод
def hand_inp():
	print("Введи три числа через пробел, строки - Enter _")
	text = []
	while True:
		h_inp = input()
		l_inp = len(h_inp.split())
		if l_inp == False:
			break
		elif l_inp != 3:
			print("введено не верное количество чисел")
		else:
			text.append(list(map(int,(h_inp.split()))))
	print("\n\n",text)
	return  text
#перебор ввода
if inp_cell1 == "1":
	print_inp(fr)
	fr = open(inp_filename,"r")
elif inp_cell1 == "2":
	inp_filename = input("Введи имя файла:_")
	fr = open(inp_filename,'r')
	print_inp(fr)
	fr = open(inp_filename,"r")
elif inp_cell1 == "3":
	inp_filename = input("Введи имя файла:_")
	while True:
		rand_n(inp_filename)
		q = input("устраивает такой файл y/n")
		if q == "y" or q == "Y":
			break
	fr=open(inp_filename,'r')
	print_inp(fr)
	fr = open(inp_filename,"r")
elif inp_cell1 == "4":
	fr = hand_inp()
else:
	print("Введи правильную команду")

#преобразование входящего файла
def convert(file):
	matrix = list(map(lambda line: line.split(),file))
	matrix_int=[]
	#приведение значений к числовому типу
	for row in matrix:
		matrix_int.append(list(map(int, row)))
	return matrix_int


#обработка условия FizzBuzz,
def fizz_bazz(trio):
	f_b = ["F","B"]	
	answer= [f_b[0] +f_b[1] if not x%trio[0] and not x%trio[1]
	 else f_b[0] if not x%trio[0] else f_b[1] if not x%trio[1]
	 else str(x)for x in range(1,trio[2]+1)]
	return answer

#преобразование списка к текстовому виду
def textrator(matrix):
	text = "\n".join(list(map(lambda listr: " ".join(listr),matrix)))
	return text

def F_B_fun(file,i):
	if i != "4":
		conv_info = convert(file)
		fr.close()
	else:
		conv_info = file

	f_b_inf = (fizz_bazz(trio) for trio in conv_info)
	text_inf = textrator(f_b_inf)
	return text_inf


rezult= F_B_fun(fr,inp_cell1)

print("Результат Fizz_Bazz:\n")
print(rezult)
#запись в файл
inp_cell2 = input("Записывать результат в файл? (y/n)__")
if inp_cell2 == "y":
	inp_cell2 = input("Запись в файл " + out_filename +"? (y/n)___")
	if inp_cell2 != "y":
		name_f = input("Введи имя файла:_")
		fw = open(name_f,"w")

	fw.write(rezult)
print("The End =)")

fw.close()
