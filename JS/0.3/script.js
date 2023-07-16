function criarTabuada() {
    var tabuada = "";
    var number1 = prompt("Escolha um numero: ");

    for (var i = 0; i < 10; i++) {
        tabuada += number1 + " x " + i +" = " + number1*i + "<br>";
    }
    var teste = document.querySelector(".teste");
    teste.innerHTML = tabuada;
}

function apagarTabuada() {
    var teste = document.querySelector(".teste");
    teste.innerHTML = "";
}

document.write("<button id='a' onclick='criarTabuada()'>Criar tabuada</button>");
document.write("<button id='b' onclick='apagarTabuada()'>Limpar tabuada</button>");
document.write("<h1 class='teste'></h1>");

let botao1 = document.getElementById("a");
botao1.style.background = "#4f4f4f";
botao1.style.padding = "5px";
botao1.style.border = "1px solid Black";
botao1.style.margin = "10px";
botao1.style.border = "1px solid Black";
botao1.style.color = "white";


let botao2 = document.getElementById("b");
botao2.style.background = "#4f4f4f";
botao2.style.padding = "5px";
botao2.style.border = "1px solid Black";
botao2.style.margin = "10px";
botao2.style.border = "1px solid Black";
botao2.style.color = "white";

