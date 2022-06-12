from time import sleep
from random import randint

pc = randint(1,3)
print('Vamos jogar....')
print('\n')
sleep(0.3)
print("""Qual sua escolha:

    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
    """)
usuario = int(input('Escolha: '))
res = ''
if usuario == 1:
    print("PEDRA!")
    if pc == 1:
        sleep(0.1)
        print('PEDRA!')
        res = 'EMPATAMOS!'
    elif pc == 2:
        sleep(0.1)
        print('PAPEL!')
        res = 'GANHEI SEU BOSTA!'
    else:
        sleep(0.1)
        print('TESOURA!')
        res = 'SORTUDO DO CARALHO!'
if usuario == 2:
    print("PAPEL!")
    if pc == 1:
        sleep(0.1)
        print('PEDRA!')
        res = 'SORTUDO DO CARALHO!'
    elif pc == 2:
        sleep(0.1)
        print('PAPEL!')
        res = 'EMPATAMOS!'
    else:
        sleep(0.1)
        print('TESOURA!')
        res = 'GANHEI SEU BOSTA!'
if usuario == 3:
    print("TESOURA!")
    if pc == 1:
        sleep(0.1)
        print('PEDRA!')
        res = 'GANHEI SEU BOSTA!'
    elif pc == 2:
        sleep(0.1)
        print('PAPEL!')
        res = 'SORTUDO DO CARALHO!'
    else:
        sleep(0.1)
        print('TESOURA!')
        res = 'EMPATAMOS!'
sleep(0.1)
print(res)
        
        
