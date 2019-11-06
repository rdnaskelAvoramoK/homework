/*
12. Дана строка 'aaa@bbb@ccc'. Замените все @ на '!' с помощью глобального поиска и замены.
 (посмотрите replace например)
*/
var st='aaa@bbb@ccc';
console.log ( st.replace ( /@/g, "!" ) )