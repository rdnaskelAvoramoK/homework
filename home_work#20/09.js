/*
09. Обратите внимание на те или иные расчеты, нужные вам в обычной жизни. 
Это может быть оплата за электричество, количество километров,
пройденных за месяц (если вы, например, ходите по одному и тому же 
маршруту каждый день), количество батонов, кофе, масла, всего чего угодно и так далее. 
Так же можете написать любую калькуляцию, нужную вам в работе. 
Представьте это в форме кода, подобного следующему:

var firstParameter = 5; //смысл переменной
var secondParameter = 10; //иной комментарий, поясняющий переменную

var somePartialResult = firstParameter*5; //суть переменной и формулы
var someOtherPartialResult = secondParameter/100500; //

var result = somePartialResult + someOtherPartialResult; //суть результата и переменной

То есть, напишите калькуляцию, которая из входных данных подсчитывает результат,
с осмысленными названиями переменных и комментариями к ним и формулам, использованным в калькуляции.

Суть - научиться правильно и осмысленно называть переменные и не только 😉
*/

let electricity_tariff_100 = 0.9, electricity_tariff_101 = 1.68; //тарифы за электричество до 100кВт и выше 100квт
let wather_cold_tariff = 13.14; //тариф холодной воды
let wather_hot_tariff = 93.22;  //тариф гоячей воды
let Sewerage_tariff = 6.696;    //тариф канализации

let Rent = Number(prompt('кварплата =','48'));                    //кварплата
let GarbageRemoval = Number(prompt('вывоз мусора = ', '82.14'));   //вывоз мусора
let GasSupply = Number(prompt('газоснабжение = ','100'));          //газоснабжение

var oldCounterIndication_electricity = Number(prompt('старые показания по свету', '1111'));     //старые показания по свету
var newCounterIndication_electricity = Number(prompt('новые показания по свету', 
    oldCounterIndication_electricity + 100));                                                   //новые показания по свету
let size_electricity = newCounterIndication_electricity - oldCounterIndication_electricity;       // разница  по свету за месяц
alert('старые показания по свету =' + oldCounterIndication_electricity +
      '; новые показания по свету =' + newCounterIndication_electricity +
       "разница  по свету за месяц = " + size_electricity);                      


var oldCounterIndication_water_hot = Number(prompt('старые показания по гор.воде', '231'));     //старые показания по гор.воде
var newCounterIndication_water_hot = Number(prompt('новые показания по гор.воде',
         oldCounterIndication_water_hot + 10));                                                 //новые показания по гор.воде
let size_wather_hot = newCounterIndication_water_hot - oldCounterIndication_water_hot;          // разница  по гор.воде за месяц
alert('старые показания по гор.воде='+oldCounterIndication_water_hot+
     '; новые показания по гор.воде=' + newCounterIndication_water_hot +
     'разница по гор.воде за месяц' + size_wather_hot);

var oldCounterIndication_water_cold = Number(prompt('старые показания по хол.воде', '231'));     //старые показания за хол.воду
var newCounterIndication_water_cold = Number(prompt('новые показания по хол.воде',
        oldCounterIndication_water_cold + 10));                                                  //новые показания за хол.воду
let size_wather_cold = newCounterIndication_water_cold - oldCounterIndication_water_cold;        // разница  по хол.воде за месяц
alert('старые показания по хол.воде='+oldCounterIndication_water_cold+
     '; новые показания по хол.воде=' + newCounterIndication_water_cold+
        'разница по гор.воде за месяц'+ size_wather_cold);

let waterSupplyAndSewerage = (size_wather_hot + size_wather_cold) * Sewerage_tariff; //подсчёт оплаты за ползование канализацией

var electricity = size_electricity <= 100 ? size_electricity * electricity_tariff_100 :
 (100 * electricity_tariff_100) + ((size_electricity - 100) * electricity_tariff_101);  //подсчёт оплаты за электричество

var wather_hot = size_wather_hot * wather_hot_tariff;           //подсчёт оплаты за гор.воду 
var wather_cold = size_wather_cold * wather_cold_tariff;        //подсчёт оплаты за хол.воду
var sum = wather_hot + wather_cold + electricity + Rent + GarbageRemoval + GasSupply; //подсчёт суммы комунальных платежей

 alert('Кварплата =' + Rent +'; вывоз мусора =' + GarbageRemoval + '; газоснабжение =' + GasSupply +
  '; Гор.вода=' + size_wather_hot + 'м3/' + wather_hot + 
  '; Хол.вода=' + size_wather_cold + 'м3/' + wather_cold + 'ползование канализацией = '+ waterSupplyAndSewerage +
  '; Итого:' + sum )