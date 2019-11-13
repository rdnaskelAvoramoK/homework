/*
2. Делаем функцию, которая принимает аргументом название тега и возварашает созданый тег.
 Потом Делаем функцию, которая принимает этот тег как аргумент и вставляет в body.
PS. createEl..., append...
*/
function createTeg (name) {
return document.createElement (`${name}`);
}
function addTag(nameTag){
    document.body.appendChild (nameTag)
}
AddTag(CreateTeg("test"))

/*
4. Делаем функцию, которая принимает в качестве аргумента id тега и если этого тега нету внутри body, то возврашает,
 что нельзя удалить этот тег, потому что в вёрстке этого тега нету. Если этот тег в вёрстке, то удаляет
*/

function dellTag(id){
	var tag = document.getElementById(id);
	if (tag === null){console.log("this tag is not in the layout")}
    else {
        var removed = tag.parentNode.removeChild ( tag ) }
    }

dellTag("myimg")

/*
5. Нужно взять и сделать функцию getInnerTextOfElement, которая принимает в качестве аргумента название например '#name'.
 То внутри делает поиск по getElementById и берет innerText и возварашает. НЕ МОЖНО использовать querySelector.
 Првоверяете аргумент. Начинается на точку или на #, чтобы вызвать тот метод, который вам нужен.
*/

function getInnerTextOfElement(event){
    if (event[0]==="#"){
        var element = document.getElementById(event.substring (1))
        };
    if  (event[0]==="."){
        var element = document.getElementsByClassName(event.substring (1))
        };
    return element
}

/*
6. Делаем функцию $(), которая может принимать аргументом название класса, айди или название просто тега.
Если это тег, то ишем по тегу и выводим эти елементы, которые мы нашли. Если это айди, то ишем по айди.
Если это класс. Тоооо, если на сайте несколько таких класов, возварашаем как массив елементов,
который нашли, если только один клас, то возвараем просто один елемент не в массиве!
 */


