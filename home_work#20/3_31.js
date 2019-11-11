/*
31. Задание на МС.  Создайте пустой массив. В цикле до n на каждой итерации запускайте prompt для ввода любых символов, полученное значение добавляйте в конец созданного массива.
 После выхода из цикла посчитайте сумму всех чисел массива и выведите в alert полученный результат
*/
var arr=[];
var SumNum = n => {
for (i=0;i<n;i++) {
    var data = prompt('input data');
        arr.push(data)};
function sumArr(data){
          return sum = data.map(
          (x) =>(isNaN(Number(x))) ? 0: +x).reduce(function(previousValue, currentValue)
          {return previousValue + currentValue})
      }
    alert(sumArr(arr))
}
SumNum(5)
