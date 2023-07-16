class Funcionario:
    def __init__(self, nome, nasc, salario):
        self.nome = nome
        self.nasc = nasc
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, projeto, nome, nasc, salario):
        super().__init__(nome, nasc, salario)
        self.projeto = projeto

    def informarProjeto(self):
        return self.projeto

class Programador(Funcionario):
    def __init__(self, lingugem, nome, nasc, salario):
        super().__init__(nome, nasc, salario)
        self.linguagem = lingugem
    
    def imformarLingugem(self):
        return self.linguagem

gerente = Gerente('Fucionario', 'Lucas','aaaa/mm/dd',1800)

print(gerente.nome)














