/*
abstração -> Entidade, Indendidade, Caracteristica, açoes 

Entidade -> ContaBancaria
Indendidade -> pessoa = new ContaBancaria()
caracteristicas -> agrncia, numeroConta, saldo, limite
abstração -> depositar, sacar, CondultaSaldo
*/

class ContaBancaria {
  constructor () {
    this.agencia = 1059
    this.numeroDaConta = 34532
    this.saldo = 90
    this.limite = 1000
  }

  depositar(valor) {this.saldo += valor}
  Sacar(valor) {return this.saldo -= valor}
  CondultaSaldo() {return this.saldo}
}

let pessoa = new ContaBancaria()

pessoa.depositar(100)
console.log(pessoa.CondultaSaldo())
pessoa.Sacar(100)
console.log(pessoa.CondultaSaldo())
