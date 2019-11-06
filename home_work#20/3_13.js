/*
13. Дана строка 'aaa bbb ccc'.
 Вырежите из нее слово 'bbb' тремя разными способами
 (через substr, substring, slice)
*/
var str='aaa bbb ccc'
console.log ( str.substr ( 0, 4 ) + str.substr (-3, str.length))
console.log ( str.substring ( 0, 4 ) + str.substring (8))
console.log ( str.slice ( 0, 4 ) + str.slice (-3, str.length))
