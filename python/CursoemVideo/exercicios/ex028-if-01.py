from random import randint

print('Pensando em um número.... de 0 a 5')
num = randint(0,5)
print('Já pensei!')

adivinhar = int(input('Em qual número eu pensei? [0 a 5]\n R:'))
if adivinhar == num:
    print('Você acertou!')
else:
    print('Você errou! Otário! Eu pensei no número {} e não no número {}!'.format(num,adivinhar))
