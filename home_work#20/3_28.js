/*
28. Создайте смешанный массив, например [1, 2, 3, ‘a’, ‘b’, ‘c’, ‘4’, ‘5’, ‘6’]. 
    Посчитайте сумму всех его чисел, включая строковые. Выведите сумму в alert.
*/

var arr=[1, 2, 3, 'a', 'b', 'c', '4', '5', '6'];
function sumArr(data){
    return sum = data.map(
    (x) =>(isNaN(Number(x))) ? 0: +x).reduce(function(previousValue, currentValue)
    {return previousValue + currentValue})
}
console.log(sumArr(arr))