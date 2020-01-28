
function ssilkaNaImgIzPrompt(){
    var img = document.getElementById('myimg');

    do {
    var link = prompt("Enter a link to the picture")}
    while (checkURL(link) == false);

    img.src = link;

    do {
    var angle = prompt("Enter image rotation angle")}
    while(isNaN(Number(angle)));

    img.style.transform = `rotate(${angle}deg)`;

    for (i=2; i<=5;i++){
        var nameImg = `$(newImg)i`
        var nameImg = document.createElement("img");
        nameImg.src = link;
        var newImg1 = document.body.appendChild(nameImg);
        var newAngle = String(Number(angle)*i);
        nameImg.style.transform = `rotate(${newAngle}deg)` };
}
function checkURL(url) {
    var regURL = /^(?:(?:https?|ftp|telnet):\/\/(?:[a-z0-9_-]{1,32}(?::[a-z0-9_-]{1,32})?@)?)?(?:(?:[a-z0-9-]{1,128}\.)+(?:com|net|org|mil|edu|arpa|ru|gov|biz|info|aero|inc|name|[a-z]{2})|(?!0)(?:(?!0[^.]|255)[0-9]{1,3}\.){3}(?!0|255)[0-9]{1,3})(?:\/[a-z0-9.,_@%&?+=\~\/-]*)?(?:#[^ \'\"&<>]*)?$/i;
    return regURL.test(url);
}


var mydata = ssilkaNaImgIzPrompt()
