/*
25. Напишите функция, которая принимает аргументом строку и
 возврашает нам строку преобразуя первую букву строки в верхний регистр.
*/

var Upper = new Function('str', 'return str.charAt(0).toUpperCase() + str.slice(1)');
console.log(Upper('qwerty'));