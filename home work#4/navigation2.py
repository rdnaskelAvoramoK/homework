my_location = int(input("""Выбери свое местоположение
1. зеленая
2. желтая
3. красная
4. коворинг
5. ресепшн
6. коричневая
7. макдональдс
8. корридор
9. уборная

локация:"""))
coordinates = {1: 11, 2: 12, 3: 13, 4: 21, 5: 22, 6: 23, 7: 31, 8:32, 9: 33}

my_location = coordinates [my_location]

while True: 
	my_location = str(my_location)
	location ={"11":"зеленая", "12":"желтая", "13":"красная", "21":"коворинг", "22":"ресепшн", "23":"коричневая", "31":"макдональдс", "32":"корридор", "33":"уборная"}
	print("\nТы находишься в локации: \"" + location[my_location] + "\"\n")
	route = ""
	border =[]

	if  int(my_location[1]) < 3:
		route += '(e) Восток ' + "\n" 
	else:
		border += "e"
	if int(my_location[1]) > 1:
		route += '(w) Запад ' + "\n"
	else:
		border += "w"
	if int(my_location[0]) < 3 and not my_location == "21":
		route += '(s) Юг' + "\n"
	else:
		border += "s"
	if int(my_location[0]) > 1 and not my_location == "31":
		route += '(n) Север' + "\n"
	else:
		border += "n"
	if my_location == "31" or my_location =="32":
		route += '(l) войти в лифт'


	travel = input("\n Оглянувшись по сторанам, можешь двигаться на : \n"
	 + route + "\n или что то другое для выхода.\n..")
	if travel in border:
		print("\nТы не можешь идти туда! Внимательней!\n")
		input()
	elif travel == "e" or travel =="l" and my_location =="31":
		my_location = int(my_location) + 1
	elif travel == "w" or travel =="l" and my_location =="32":
		my_location = int(my_location) - 1
	elif travel == "s":
		my_location = int(my_location) + 10
	elif travel == "n":
		my_location = int(my_location) - 10
	elif travel == "t":
		my_location_t = int(input("""\nВнимание! Ты вызвал телепорт в 
1. зеленая
2. желтая
3. красная
4. коворинг
5. ресепшн
6. коричневая
7. макдональдс
8. корридор
9. уборная 

локация:"""))
		if my_location_t not in coordinates:
			print("\nТакой локации не существует. Телепорт закрыт...\n")
			input()

		else:
			my_location = coordinates [my_location_t]
	else:
		 break