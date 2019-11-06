/*
18. Дана строка 'я учу javascript!'.
 Вырежите из нее слово 'учу' и слово 'javascript' тремя разными способами 
 (через substr, substring, slice).
*/
var str='я учу javascript!';
console.log ( str.substr ( 2, 3 ) , str.substr (6,10));
console.log ( str.substring ( 2, 5 ),  str.substring (6,16));
console.log ( str.slice (2, 5 ), str.slice ( 6, -1));