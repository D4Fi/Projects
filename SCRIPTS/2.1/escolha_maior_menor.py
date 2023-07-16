import random

number = random.randint(1,10)
start = True

while start:
    user_number = int(input('Escolha um numero:: '))
    if user_number > number:
        print('Menor!')
    elif user_number < number:
        print('Maior!')
    elif user_number == number:
        print('Você ganhou!!!')
        break