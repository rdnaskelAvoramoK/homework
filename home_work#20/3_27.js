/*
27. Напишите функция, которая принимает аргументом строку и 
преобразуйте например 'var_test_text' в 'varTestText'.
 Функция, конечно же, должен работать с любыми аналогичными строками.
*/
//var strings = ;
function newString (strings){return (strings.split('_').map((x) => { 
return 
x === strings[0] ? x: x.charAt(0).toUpperCase() +x.substring(1, x.length)}).join(""))
};
console.log(newString("_var_test__text_data_base_"));