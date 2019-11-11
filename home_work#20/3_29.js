/*29. Сгенерируйте массив из n случайных чисел с двумя знаками после запятой.
 Переберите массив и распечатайте в консоли значения его элементов,
 возведенные в пятую степень, не используя функцию Math.pow().*/
var arr=[];
function randomArr(n){for (i =0 ;i<=n; i++) {var gen = arr.push((Math.random()*n+n/7).toFixed(2))};
return arr};
newarr = randomArr(10);
newarr.forEach(function(item){return console.log(item,item**5)})