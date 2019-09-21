import sys
inp_filename = sys.argv[1]
out_filename = sys.argv[2]
fr = open(inp_filename,"r")
fw = open(out_filename,"w")
f_b = ["F","B"]

#преобразование входящего файла
matrix = [x.split() for x in (line for line in fr)]

#приведение значений к числовому типу
matrix_int = [[int(cell) for cell in row] for row in matrix ]

#обработка условия FizzBuzz,
answer= [[f_b[0] +f_b[1] if not x%a[0] and not x%a[1] else 
f_b[0] if not x%a[0] else f_b[1] if not x%a[1] else str(x) 
for x in range(1,a[2]+1)] for a in matrix_int]

#преобразование списка к текстовому виду
text = "\n".join([" ".join(cell) for cell in answer])

#запись в файл
fw.write(text)
print(text)
fr.close()
fw.close()
