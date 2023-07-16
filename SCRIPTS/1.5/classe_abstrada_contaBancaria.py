from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def consultar_saldo(self):
        return self.saldo

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo_inicial, limite):
        super().__init__(saldo_inicial)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor * 1.02

    def depositar(self, valor):
        self.saldo += valor * 1.01
















