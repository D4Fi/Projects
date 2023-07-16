/*
A classe "Animal" tem um construtor que recebe o nome e o tipo do animal,
e um método "comer". As classes "Cachorro" e "Passaro" herdam de "Animal" e
adicionam suas próprias propriedades e métodos, como a raça e o latido para
"Cachorro", e a espécie e o voo para "Passaro". A classe "Papagaio" herda de
"Passaro" e adiciona sua própria propriedade "cor" e o método "falar".
*/

class Animal {
    constructor(cor, tamanho, peso) {
        this.cor = cor
        this.tamanho = tamanho
        this.peso = peso
    }
    
    dormir() {console.log('Dormi!')}
}

class Cachorro extends Animal {
    constructor() {
        super()
        this.orelha = 'Larga'
    }
    correr() {console.log('Correr!')}
    rosnar() {console.log('Rosnar!')}
}

class Passaro extends Animal {
    constructor(bico, cor, tamanho, peso) {
        super(cor, tamanho, peso)
        this.bico = bico
    }
    voar() {console.log('Voar!')}
}

class Papagaio extends Passaro {
    constructor(sabeFalar, bico, cor, tamanho, peso) {
        super(bico, cor, tamanho, peso)
        this.sabeFalar = sabeFalar
    }
    falar() {console.log('Falar!')}
}

let cachorro = new Cachorro()
let passaro = new Passaro()
let papagaio = new Papagaio(true, 'Fino', 'black', 10, 100)
let papagaio2 = new Papagaio(false, 'Fino', 'black', 10, 100)

cachorro.dormir()
passaro.dormir()
papagaio.falar()

console.log(papagaio)
console.log(papagaio2)