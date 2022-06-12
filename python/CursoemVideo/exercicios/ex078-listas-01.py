lista = []
for num1 in range(0,5):
    lista.append(int(input(f'Digite um valor inteiro para a Posição {num1}: ')))
print('-='*35)
print(f'Lista de valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} na(s) posição(ões): ', end = '')
for num2 in range(0,len(lista)):
    if lista[num2] == max(lista):
        print(f'{num2}...', end = ' ')
print(f'\nO menor valor digitado foi {min(lista)} na(s) posição(ões): ', end = '')
for num3 in range(0,len(lista)):
    if lista[num3] == min(lista):
        print(f'{num3}...', end = ' ')
