

function ssilkaNaImgIzPrompt(){
    var img = document.getElementById('myimg');
    img.src = prompt("Enter a link to the picture");
    var angle = prompt("Enter image rotation angle")
    img.style.transform = `rotate(${angle}deg)`;
    var newImg = document.body.appendChild(img)
    return [img,angle]
}
var mydata = ssilkaNaImgIzPrompt()