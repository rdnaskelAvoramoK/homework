/*
2.Задача. Создайте переменную str и присвойте ей значение 'abcde'.
 Обращаясь к отдельным символам этой строки выведите на экран символ 'a', символ 'b', символ 'e'.
Перебираем через цикл строку и при переборе строки если текушее значение в цикле
 будет равно 'a', 'b', 'e' - вывести через console 'Я знаю эту букву'
*/
let str = 'abcde'
for (lit of str) {if (lit == 'a' | lit == 'b' | lit == "e") console.log(lit,' Я знаю эту букву')}