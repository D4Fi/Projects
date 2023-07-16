


array = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

style = f'''
{array[0]}|{array[1]}|{array[2]}
------
{array[3]}|{array[4]}|{array[5]}
------
{array[6]}|{array[7]}|{array[8]}'''



def vencedor(array):
    win = [array[0] == array[1] == array[2], 
           array[3] == array[4] == array[5], 
           array[6] == array[7] == array[8], 
           array[0] == array[3] == array[6], 
           array[1] == array[4] == array[7], 
           array[2] == array[5] == array[8], 
           array[0] == array[4] == array[8], 
           array[2] == array[4] == array[6]]
    
    return any(win)

def jogadas(caracter):
    global array
    jogada = int(input('Digite a jogada:: '))
    array[jogada] = caracter
 

start = true
while start:
    

    start = vencedor()




 

















