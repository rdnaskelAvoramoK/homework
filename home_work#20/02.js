/*
02. Создайте три переменные с любыми числовыми значениями.
 Используя условный оператор  и не используя логические, найдите минимальное число
 и отобразите на экране имя переменной и ее значение.
*/
let a = -77, b = 13, c = -19
if (a < b) {
    if (a < c) console.log("a", a)
    else {console.log("c", c)}}
else {
    if (b < c) console.log("b", b)
    else {console.log("c", c)}}
    