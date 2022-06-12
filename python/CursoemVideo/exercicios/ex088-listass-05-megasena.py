from random import randint
from time import sleep
lista = []
listaAux = []
jogos = int(input('Quantidade de jogos: '))
for j in range(0,jogos):
    listaAux.clear()
    for k in range(0,6):
        n = (randint(1,60))
        if n not in listaAux:
            listaAux.append(n)
        listaAux.sort()
    lista.append(listaAux[:])
print('-='*3 + ' SORTEANDO {} JOGOS '.format(jogos) + '-='*3)
for numero, jogo in enumerate(lista):
    print(f'Jogo {numero+1}: {jogo}')
    sleep(0.6)
print('-='*5 + ' BOA SORTE!' + '-='*5)
#problema: se gerar numero igual ele n coloca e n forma 6 numeros
