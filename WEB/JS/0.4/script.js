function sum() {
    var number2 = prompt('Digite um numero: ');
    number2 = parseFloat(number2)
    number += number2;
    doc.innerHTML = number;
}

function sub() {
    var number2 = prompt('Digite um numero: ');
    number2 = parseFloat(number2)
    number -= number2;
    doc.innerHTML = number;
}

function mul() {
    var number2 = prompt('Digite um numero: ');
    number2 = parseFloat(number2)
    number *= number2;
    doc.innerHTML = number;
}

function div() {
    var number2 = prompt('Digite um numero: ');
    number2 = parseFloat(number2)
    number /= number2;
    doc.innerHTML = number;
}

document.write("<button onclick='sum()'>+</button>");
document.write("<button onclick='sub()'>-</button>");
document.write("<button onclick='mul()'>*</button>");
document.write("<button onclick='div()'>/</button>");
document.write("<h1 id='teste'></h1>");

var doc = document.getElementById('teste');
var number = prompt('Digite um numero: ');
number = parseFloat(number)
doc.innerHTML = number;






















