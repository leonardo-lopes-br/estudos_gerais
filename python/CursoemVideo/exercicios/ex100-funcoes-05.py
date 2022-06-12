from random import randint
numeros = []
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end = ' ')
    for i in range(0,5):
        numeros.append(randint(0,100))
        print(f'{numeros[i]}', end = ' ')
    print()
def somaPar(list):
    result = 0
    for j in range(0,len(list)):
        if list[j] % 2 == 0:
            result += list[j]
    print(f'Somando os valores pares de {list} temos {result}')
sorteia(numeros)
somaPar(numeros)
