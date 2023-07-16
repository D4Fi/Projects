'''
abstração -> Entidade, Indendidade, Caracteristica, açoes

Entidade -> ContaBancaria
Indendidade -> pessoa = new ContaBancaria()
caracteristicas -> agrncia, numeroConta, saldo, limite
abstração -> depositar, sacar, ConsultaSaldo
'''

class ContaBancaria:
    def __init__(self):
        self.agencia = 1059
        self.numeroDaConta = 34532
        self.saldo = 90
        self.limite = 1000

    def depositarSaldo(self, valor): self.saldo += valor
    def sacar(self, valor): self.saldo -= valor
    def consultarSaldo(self): return self.saldo

pessoa = ContaBancaria()

pessoa.depositarSaldo(100)
print(pessoa.consultarSaldo())
pessoa.sacar(100)
print(pessoa.consultarSaldo())



