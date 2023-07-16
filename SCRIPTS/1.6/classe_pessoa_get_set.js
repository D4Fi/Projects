class Pessoa {
    constructor(nome, idade, cpf){
        this._nome = nome;
        this._idade = idade;
        this._cpf = cpf;
    }

    get nome() {
        return this._nome;
    }

     get idade() {
        return this._idade;
    }

    get cpf() {
        return this._cpf;
    }

    set nome(nome) {
        this._nome = nome
    }

    set idade(idade) {
        this._idade = idade
    }

    set cpf(cpf) {
        this._cpf = cpf
    }
}

let pessoa = new Pessoa('Ingride', 36, 90909009)
console.log(pessoa)
console.log('-----------------')

pessoa.nome = 'Luca'
pessoa.idade = 89
pessoa.cpf = 89899889
console.log(pessoa)