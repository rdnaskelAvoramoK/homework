/*
10. Дан массив числами, например: [10, 20, 30, 50, 235, 3000].
Выведите на экран только те числа из массива, которые начинаются на цифру 1, 2 или 5.
*/
var arr=[10, 20, 30, 50, 235, 3000];
for (i of arr) { var str = String(i)
    if (str[0]==='1'| str[0]==='2'| str[0]==='5') {alert(str)}}