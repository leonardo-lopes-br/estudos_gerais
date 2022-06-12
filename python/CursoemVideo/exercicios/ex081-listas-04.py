lista = []
resposta = ' '
while resposta != 'N':
    lista.append(int(input('Digite um número inteiro: ')))
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta not in 'SN':
        while resposta not in 'SN':
            resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
lista.sort(reverse = True)
print('-='*35)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
