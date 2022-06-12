resposta = ' '
lista = []
pares = []
impares = []
n = 0
while resposta != 'N':
    n = int(input('Digite um valor: '))
    lista.append(n)
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta not in 'SN':
        while resposta not in 'SN':
            resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-='*30)
print(f'Lista de valores: {lista}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
