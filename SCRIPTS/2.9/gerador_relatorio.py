import os
import re
import sys 

class ExtrairDados:
    file: list[str]

    def __init__(self, path: str) -> None:
         with open(path, 'r') as file:
            self.file = file.read().split()

    ###########################
    #        Cabeçalho        #
    ###########################
    def numero_da_empresa():
        return re.sub(r'[0-9]+','',self.file[2])  + ' ' + self.file[3]

    def nome_cidada(self):
        nome = self.file[15]
        return nome[0:20]
    
    def numero_da_empresa(self):
        numero = self.file[1]
        return numero[1:3]+'.'+numero[3:6]+'.'+numero[6:9]+'/'+numero[9:13]+'-'+numero[13:15]

    def nome_banco(self):
        return self.file[4] 
    
    def cep(self):
        cep = self.file[15]
        return cep[20:25] +'-'+cep[25:28]
    
    def sigla_estado(self):
        sigla_estado = self.file[15]
        return sigla_estado[28:]

    def nome_rua(self):
        return self.file[11] + ' ' + self.file[12] + ' ' +  self.file[13],

    def cabecalho(self) -> dict:
        return {
            'nome_empresa': re.sub(r'[0-9]+','',self.file[2])  + ' ' + self.file[3],
            'numero_de_inscricao_da_empresa': extends.numero_da_empresa(),
            'nome_banco': extends.nome_banco(),
            'nome_rua':extends.nome_rua(),
            'numero_local':self.file[14],
            'nome_cidada': extends.nome_cidada(),
            'cep': extends.cep(),
            'sigla_estado':extends.sigla_estado(),
        }

    ###########################
    #         detalhes        #
    ###########################
    def nome_favorecido(self):
        nome = re.sub(r'[0-9]+','',self.file[16]) + ' ' +self.file[17]
        return nome[1:]

    def data_pagamento(self):
        data_pagamento = self.file[20]
        data = data_pagamento[0:8]
        return data[0:2]+'/'+data[2:4]+'/'+data[4:]

    def valor_pagamento(self):
        pagamento_1 = self.file[20]
        pagamento_2 = self.file[27]
        pagamento_3 = self.file[34]
        return [pagamento_1[-3]+','+pagamento_1[-3:-1],
                pagamento_2[-5:-2]+','+pagamento_2[-3:-1],
                pagamento_3[-7:-5] +'.'+pagamento_3[-5:-2]+','+pagamento_3[-3:-1]]


    def detalhes(self) -> dict:
        return {
            'nome_favorecido': extends.nome_favorecido(),
            'data_pagamento': extends.data_pagamento(),
            'valor_pagamento': extends.valor_pagamento(),
            'numero_do_documento_atribuido_pela_empresa': [self.file[19], self.file[26], self.file[33]],
            'forma_de_lancamento': 'Credito em conta corrente',
        }

def gerarcss():
    css = ''
    for i, in extends.cabecalho():
        i += i+','
if __name__ == '__main__':
   extends = ExtrairDados(sys.argv[1])
   print('===========================================================================')
   for i,ii in zip(extends.cabecalho(), extends.cabecalho().values()):
       print(i,',',ii)
   print('===========================================================================')
   for i,ii in zip(extends.detalhes(), extends.detalhes().values()):
       print(i,'::',ii)
