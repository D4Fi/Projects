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

//Polimorfismo para sobrescrever o metodo voar
class Avestrus extends Passaro {
    constructor() {
        super('Grade', 'Branco', 390, 3000)
    }

    enterrarCabeca() {console.log('Enterrar!')}
    voar() {console.log('Nao sabe voar!')}
}

let avestrus = new Avestrus()

avestrus.enterrarCabeca()
avestrus.voar()
console.log(avestrus)
