matriz = []
pares = terceiraCol = maior2 = 0
for i in range(0,3):
    for j in range(0,3):
        n = int(input(f'Digite um valor para [{i},{j}]: '))
        matriz.append(n)
        if j == 2:
            terceiraCol += n
        if i == 1:
            if n > maior2:
                maior2 = n
print('-='*30)
for m in range(0,len(matriz)):
    if matriz[m] % 2 == 0:
        pares += matriz[m]
    if m < 2:
        print("[" + '{}'.format(matriz[m]) + "]", end = ' ')
    elif m == 2:
        print("[" + '{}'.format(matriz[m]) + "]")
    elif m < 5:
        print("[" + '{}'.format(matriz[m]) + "]", end = ' ')
    elif m == 5:
        print("[" + '{}'.format(matriz[m]) + "]")
    elif m < 8:
        print("[" + '{}'.format(matriz[m]) + "]", end = ' ')
    else:
        print("[" + '{}'.format(matriz[m]) + "]")
print('-='*30)
print('A soma dos valores pares digitados é: {}'.format(pares))
print(f'A soma dos valores da terceira coluna é: {terceiraCol}')
print(f'O maior valor da segunda linha é: {maior2}')
