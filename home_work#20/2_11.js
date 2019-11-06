/*
11. Дошли? Прекрасно.
Напишите скрипт, который считает количество секунд в часе, в сутках, в месяце.

Спрашиваем у пользователя через prompt число.
Если пользователь ввёл 10h, то мы выводим ему количество секунд за 10 часов.
Если пользователь ввёл 10d, то мы выводим ему количество секунд за 10 дней.
Если пользователь ввёл 10w, то мы выводим ему количество секунд за 10 недел.
Если пользователь ввёл 10m, то мы выводим ему количество секунд за 10 месяц.

Проверяем то, что в конце)
*/
let data_time = prompt("Введи чило и объект времени(h,d,w,m) без пробелов")
let index = data_time.length-1
if (data_time[index] =='h') { alert(data_time + ' is '+ parseInt(data_time)*3600 + 'sec')}
if (data_time[index] =='d') { alert(data_time + ' is '+ parseInt(data_time)*3600*24 + 'sec')}
if (data_time[index] =='w') { alert(data_time + ' is '+ parseInt(data_time)*3600*24*7 + 'sec')}
if (data_time[index] =='m') { alert(data_time + ' is '+ parseInt(data_time)*3600*24*7*30 + 'sec')}
if (data_time[index]!='h' & data_time[index]!='d' & data_time[index]!='w' & data_time[index]!='m')
   {alert('формат времени указан не верно')}