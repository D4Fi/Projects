import random

def escolha_letra():
    letra = input('Ecolha uma letra: ')
    return letra

def escolha_palavra(palavra_lsta):
    return random.choice(palavra_lsta)

palavra = escolha_palavra(['casa', 'uva', 'prssoa'])

password = list((len(palavra))*'-')

while True:
    print(password)

    escolha = escolha_letra()
    if escolha in palavra:
        for i, ii in enumerate(palavra):
            if ii == escolha:
                password[int(i)] = ii

    if ''.join(password) == palavra:
        print('Voce ganhou!!!!!')
        print(password)
        break














