matriz = []
for i in range(0,3):
    for j in range(0,3):
        n = int(input(f'Digite um valor para [{i},{j}]: '))
        matriz.append(n)
for m in range(0,len(matriz)):
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
