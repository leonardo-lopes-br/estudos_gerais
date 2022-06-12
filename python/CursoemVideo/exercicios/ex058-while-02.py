from random import randint
pc = randint(0,10)
palpite = -1
cont = 1
print('Pensei em um número de 0 a 10! Tente Adivinhar!\n')
while palpite != pc:
    palpite = int(input('Em qual número eu pensei? [0 a 10]: '))
    if palpite != pc:
        cont += 1
        if palpite > pc:
            print('\nMenos.... Tente Novamente!\n')
        elif palpite < pc:
            print('\nMais.... Tente Novamente!\n')
print('\nPARABÉNS! Você acertou! Eu pensei justamente no número {} e você precisou de {} tentativa(s)!'.format(pc,cont))
