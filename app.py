import random
import os

input("Aperte ENTER para começar:")


def inicio():
    os.system('clear')
    print('#'*60)       
    print('foi gerado um número aleatório entre 1 e 100, advinhe qual é!')
    global myNumber, number
    myNumber = random.randrange(1,100)
    number = int(input('Chute um número entre 1 e 100:'))

inicio()
while True:
    if number != myNumber:
        if number > myNumber:
            print('Chute um número menor')
        else:
            print('Chute um número maior')
        number = int(input('Chute um número entre 1 e 100:'))
    else:
        print(f'Parabéns! Você chutou o valor certo: {myNumber}')        
        if input('Gostaria de tentar novamente?(s/n)') == 'n':
            print('#'*60)       
            print('Obrigado por participar!')
            break
        else:                 
            inicio()
