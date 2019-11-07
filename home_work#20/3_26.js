/*
26. Напишите функция, которая принимает аргументом строку и возврашает
 нам строку преобразуя последнюю букву строки в верхний регистр.
*/

var uppeR = new Function('str', 'return str.slice(0,-1) + str.charAt(str.length-1).toUpperCase()');
console.log(uppeR('abcde'));