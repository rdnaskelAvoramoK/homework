function ssilkaNaImgIzPrompt(){
    var img = document.getElementById('myimg');
    
    var link = prompt("Enter a link to the picture");
    img.src = link
    var angle = prompt("Enter image rotation angle")
    img.style.transform = `rotate(${angle}deg)`;
    
    for (i=2; i<=5;i++){
    var nameImg = `$(newImg)i`
    var nameImg = document.createElement("img");
    nameImg.src = link
    var newImg1 = document.body.appendChild(nameImg);
    var newAngle = String(Number(angle)*i);
    nameImg.style.transform = `rotate(${newAngle}deg)` }
}
var mydata = ssilkaNaImgIzPrompt()
