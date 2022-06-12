numeros = (float(input('Digite um valor: ')),float(input('Digite um valor: ')),float(input('Digite um valor: ')),
           float(input('Digite um valor: ')))
print(f'O valor 9 apareceu {numeros.count(9)} vez(es)')
if 3 not in numeros:
    print('O valor 3 não foi digitado!')
else:
    print(f'O primeiro valor 3 foi digitado na posição {numeros.index(3)+1}')
print('Os valores pares digitados foram: ', end = '')
for num in range(0,len(numeros)):
    if numeros[num] % 2 == 0:
        print(numeros[num], end = ' ')