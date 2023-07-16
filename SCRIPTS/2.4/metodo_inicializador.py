class MetodoIniciador:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'nome: {self.nome}, idade: {self.idade}'

teste = MetodoIniciador('LUCAS', '26')
print(teste)
