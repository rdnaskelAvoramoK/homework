/*
34. Используя вложенные циклы, сформируйте двумерный массив, содержащий таблицу умножения:
 "1x1=1; 2x1=1"
 "1x2=2; 2x2=4"
И выходим и останавливаем цикл, когда будет 6 умножнить на 6
*/
for (i=1;i<=6;i++) {
var arr="", arr2="";
    for (j=1;j<=6; j++){
        var str =i+"x"+j+"="+(i*j)+';';
        var arr2=arr.concat(arr2,str)
    }
console.log(arr2)
}