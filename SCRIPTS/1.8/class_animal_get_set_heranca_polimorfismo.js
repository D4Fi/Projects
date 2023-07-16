class Animal {
    constructor(idade, cor) {
        this._idade = idade
        this._cor = cor
    }

    get idede() {
        return this.idade
    }

    get cor() {
        return this.cor
    }

    set idade(newIdade) {
        this.idade = newIdade
    }

    set cor(newCor) {
        this.cor = newCor
    }

    falar() {}
}

class Cachorro extends Animal {
    constructor(idade, cor) {
        super(idade, cor)
    }

    falar() {
        console.log('Auu! Auu!')
    }
}

class Gato extends Animal {
    constructor(idade, cor) {
        super(idade, cor)
    }

    falar() {
        console.log('Miauu!')
    }
}

let cachorro = new Cachorro(3, 'Gray')
console.log(cachorro)
cachorro.falar()
console.log('--------------------------')

let gato = new Gato(6, 'red')
console.log(gato)
gato.falar()