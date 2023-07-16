class Pessoa:
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def cpf(self):
        return self._cpf

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def __str__(self):
        return f'Nome: {self._nome}\nIdade: {self._idade}\nCpf: {self._cpf}'


pessoa = Pessoa('Ingride', 45, 999999999)
print(pessoa)
print('-----------------')

pessoa.nome = 'Manu'
pessoa.idade = 78
pessoa.cpf = 4243465646
print(pessoa)