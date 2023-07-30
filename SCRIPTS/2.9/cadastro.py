class Cliente:
    '''
    class base para o ser hedada:
    '''
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade 
    
    @property
    def nome(self)-> None:
        return self.__nome 

    @nome.setter
    def nome(self, new_name)-> None:
        self.__nome = new_name
    
    def falar(self)-> str:
        '''
        funcao para falar
        '''
        return 'afdsf'

class PessoaFisica(Cliente):
    '''
    herança de Cliente 
    '''
    def __init__(self,
            cpf: str,
            nome: str,
            idade: int):
        
        super().__init__(nome, idade)
        self.cpf = cpf

if __name__ ==  '__main__':
    p1 = Cliente('Lucas', 26)
    print(p1.nome)

    p2 = PessoaFisica('5685', 'lucas', '98') 
    print(p2.falar())























