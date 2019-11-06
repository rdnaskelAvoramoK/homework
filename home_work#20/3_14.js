/*
14. В переменной date лежит дата в формате '2025-12-31'. Преобразуйте эту дату в формат '31/12/2025'.
*/
var date='2025-12-31';
console.log(date.slice ( -2, date.length ) + '/' + date.slice ( 5,7 ) + '/' + date.slice ( 0,4))