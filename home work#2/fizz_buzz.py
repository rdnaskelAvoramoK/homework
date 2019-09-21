print('input fizz number')
fizz = int(input())
print('input buzz number')
buzz = int(input())
print('input last number for calculation')
num = int(input())
list_f_z=""
for i in range(1, num+1):
    if not i%fizz and i%buzz:
        list_f_z += "F "
    elif not i%buzz and i%fizz:
        list_f_z += "B "
    elif not i%buzz and not i%fizz:
        list_f_z += "FB "
    else:
        list_f_z += str(i) + " "
print(list_f_z)