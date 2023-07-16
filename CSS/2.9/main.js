
var largura = 0
var altura= 0
var number = 1
var tempo = 11

function janela() {
    largura = window.innerWidth
    altura = window.innerHeight
    console.log(altura, largura)
}


var cronometro = setInterval(function() {
    tempo -= 1
    if (tempo < 0) {
        clearInterval(cronometro)
        clearInterval(criamosca)
        window.location.href= 'vitoria.html'
    }
    else {
        document.getElementById('relogio').innerHTML = tempo
    }
}, 1000)


function x() {
    if (document.getElementById('mosquito')) {
        document.getElementById('mosquito').remove()
        if (number > 3) {
            window.location.href= 'fim_de_jogo.html'
        }
        else{
            document.getElementById('vida' + number).src = 'image/coracao_vazio.png'
            number++
        }
    }
    var axis_x = Math.floor(Math.random() * largura) - 90
    var axis_y = Math.floor(Math.random() * altura) - 90

    axis_x = axis_x < 0 ? 0 : axis_x
    axis_y = axis_y < 0 ? 0 : axis_y

    var mosquito = document.createElement('img')
    mosquito.src = 'image/mosca.png'
    mosquito.className = tipo() + ' ' + figLado()
    mosquito.style.left = axis_x + 'px'
    mosquito.style.top = axis_y + 'px'
    mosquito.style.position = 'absolute'
    document.body.appendChild(mosquito)
    mosquito.id = 'mosquito'
    mosquito.onclick = function() {this.remove()}
}

function tipo() {
    var size = Math.floor(Math.random() * 3)
    switch (size) {
        case 0: return 'mosca1'
        case 1: return 'mosca2'
        case 2: return 'mosca3'
    }
}

function figLado() {
    var lado = Math.floor(Math.random() * 2)
    switch (lado) {
        case 0: return 'ladoA'
        case 1: return 'ladoB'
    }
}

janela()









































    
