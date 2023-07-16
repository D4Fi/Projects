from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, idade, cor):
        self._idade = idade
        self._cor = cor

    @property
    def idade(self):
        return self._idade

    @property
    def cor(self):
        return self._cor

    @idade.setter
    def idade(self, newIdade):
        self._idade = newIdade

    @cor.setter
    def cor(self, newCor):
        self._cor = newCor

    def falar(self):
        ...
    def

class Cachorro(Animal):
    def __init__(self, idade, cor):
        super().__init__(idade, cor)

    def falar(self):
        print('Falar: Auu! Auu!')


class Gato(Animal):
    def __init__(self, idade, cor):
        super().__init__(idade, cor)

    def falar(self): print('Falar: Miauuu!')


cachorro = Cachorro(2, 'Rex')
cachorro.falar()
print('idade:', cachorro.idade, '\nNome:', cachorro.cor)
print('-------------------------------')
gato = Gato(2, 'Rex')
gato.falar()
print('idade:', gato.idade, '\nNome:', gato.cor)
