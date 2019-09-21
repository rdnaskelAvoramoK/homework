import sys
inp_filename = sys.argv[1]
out_filename = sys.argv[2]
fr = open(inp_filename,"r")
fw = open(out_filename,"w")
for line in fr:
	st = line.split()
	fizz = int(st[0])
	buzz =int(st[1])
	num = int(st[2])
	list_f_z = ""
	for i in range(1,num + 1):
		if not i%fizz and i%buzz:
			list_f_z += "F "
		elif i%fizz and not i%buzz:
			list_f_z += "B "
		elif not i%fizz and not i%buzz:
			list_f_z += "FB "
		else:
			list_f_z += str(i) + " "
	list_f_z += "\n"
	print(list_f_z)
	fw.write(list_f_z)
fr.close()
fw.close()