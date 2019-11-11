/*
30. Создайте массив со значениями: ‘AngularJS’, ‘jQuery’
 a. Добавьте в начало массива значение ‘Backbone.js’
 b. Добавьте в конец массива значения ‘ReactJS’ и ‘Vue.js’
 c. Добавьте в массив значение ‘CommonJS’ вторым элементом
 d. Найдите и удалите из массива значение ‘jQuery’, выведите его в alert со словами “Это здесь лишнее”
 z. Сделайте массив и назовите dlyaLyudshix, перебирает массив, где только удалили ‘jQuery’,
     и перебирайте этот массив и если вы найдёте там значние ‘Vue.js’, то положите в массив с названием dlyaLyudshix
*/
var arr = ['AngularJS', 'jQuery'];
var newArr = arr.unshift('Backbone.js');
var newArr = arr.push('ReactJS', 'Vue.js');
var newArr = arr.splice(2,0,"CommonJS");
var searchWord = "jQuery"
var newArr = arr.splice(arr.findIndex(arr => arr === searchWord),1);
alert(searchWord + ' Это здесь лишнее');

var searchWord = "Vue.js"
var index = arr.findIndex(arr => arr === searchWord)
var dlyaLyudshix =  arr.slice(index,index+1);