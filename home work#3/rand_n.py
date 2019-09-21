import random
t = open("file_for_random.txt",'w')
qt_l = int(input("Enter the number of lines____",))
qty = int(input("Enter the maximum number in the range ____",))
for x in range(1,qt_l):
	last_n = random.randint(10,qty)
	fizz = random.randint(2,last_n//3)
	buzz = random.randint(2,last_n//5)
	if fizz == buzz:
		buzz = random.randint(2,last_n//7)
	line = str(fizz) + " " + str(buzz) + " " + str(last_n) + "\n"
	t.write(line) 
t.close()