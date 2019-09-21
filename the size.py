
outerwear={
"s":{1: 40, 2: 34, 3: 36, 4: 38, 5: 8,6: 6},
"m":{1: 42, 2: 36, 3: 38, 4: 40, 5: 10,6: 8},
"l":{1: 46, 2: 38, 3: 40, 4: 42, 5: 12,6: 10},
"xl":{1: 50, 2: 44, 3: 46, 4: 48, 5: 18,6: 16},
"xxl":{1: 54, 2: 48, 3: 50, 4: 52, 5: 22,6: 20}
            }

sizes = input("enter international outerwear size __")
selection=outerwear.get(sizes.lower())

t=("Russia", ('Belgium/Germany/Netherlands/Norway/Finland/Sweden'),
    ('Sweden/France'),'Italy','Great_Britain','USA')

countrie = int(input("\nplease input:\n" + "\n".join([str(i[0]+1) + 
	" if your choise is " + str(i[1]) for i in enumerate(t)])+"\n____"))

print(sizes," is ",selection.get(countrie)," in ", t[countrie-1])