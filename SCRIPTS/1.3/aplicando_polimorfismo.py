class Animal:
    def __init__(self, color, size, weight):
        self.color = color
        self.size = size
        self.weight = weight

    def dormir(self):
        print('Dormi!')

    def voar(self):
        print('Voar!')

    def __str__(self):
        animal = {
            'color': self.color,
            'size': self.size,
            'weight': self.weight
        }
        return f'{animal}'

class Cachorro(Animal):
    def __init__(self, color, size, weight):
        super().__init__(color, size, weight)
        self.olhera = 'Larga!'

    def voar(self):
        print('Nao voa!')

class Passaro(Animal):
    def __init__(self, bico, color, size, weight):
        super().__init__(color, size, weight)
        self.bico = bico

class Papagaio(Animal):
    def __init__(self, sabeFalar, color, size, weight):
        super().__init__(color, size, weight)
        self.sabeFalar = sabeFalar

class Avestruz(Animal):
    def __init__(self, color, size, weight):
        super().__init__(color, size, weight)

    def voar(self):
        print('Nao sabe voar')

cachorro = Cachorro('Black', 2090, 1000)
cachorro.dormir()
cachorro.voar()
print(cachorro)

print('--------------------')
passaro = Passaro('Longo', 'Red', 4000, 999)
passaro.dormir()
print(passaro)

print('--------------------')
papagaio = Papagaio('Sim', 'Red', 4000, 888)
papagaio.dormir()
print(papagaio)

print('--------------------')
avestruz = Avestruz('Red', 4000, 888)
avestruz.dormir()
avestruz.voar()
print(avestruz)