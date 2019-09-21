x = int(input("Enter number\n__",))
i=1
multiple=""
if not x%2:
	print(str(x)+" is even number")
elif x%2 and not x%3 and not x%5 and x%10:
	print(str(x)+" is odd number, multiple of 3 and 5 at the same time, but  but not a multiple of 10")
else:
	print(str(x)+" is odd number")
while  i < x:
	if not x%i:
		multiple += str(i)+", "
	i += 1
multiple = multiple[:-2] + "are multiple of number " + str(x)
print(multiple)

# digit number
digit = len(str(x))
sample = ""
for j in range(len(str(x))):
	sample += str(x)[j]+"*10**"+str(digit-1) + "+"
	digit -=1
sample = sample[:-1]+"="+str(x)
print(sample)

test = True
print('ttt' if test  else 'fff')

print("Give it to me!")
number = int(input())

if number >= 100:
	print ("Thanks, man!")
elif number > 10 and number <100:
	print("OK :(")
else:
	print ("WHAAAT????")
if number > 1000:
	print("!!!!WOOOOWWWW!!!")