lista = []
n = int(input('Digite um valor: '))
print('Valor adicionado com sucesso!')
lista.append(n)
resposta = ' '
while resposta != 'N':
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'S':
        n = int(input('Digite um valor: '))
        if n in lista:
            print('Valor duplicado! Não vou adicionar...')
        else:
            lista.append(n)
            print('Valor adicionado com sucesso!')
lista.sort()
print('-='*30)
print('Os valores digitados foram: {}'.format(lista))
