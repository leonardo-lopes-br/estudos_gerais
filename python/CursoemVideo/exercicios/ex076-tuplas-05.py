c = cont = 0
listagem =(input('Produto: '),float(input('Preço: ')),input('Produto: '),float(input('Preço: ')),input('Produto: '),float(input('Preço: ')),
           input('Produto: '),float(input('Preço: ')),input('Produto: '),float(input('Preço: ')),input('Produto: '),float(input('Preço: ')),
           input('Produto: '),float(input('Preço: ')),input('Produto: '),float(input('Preço: ')),input('Produto: '),float(input('Preço: ')))
print('-'*50)
print(' '*15 + 'LISTAGEM DE PREÇOS' + ' '*10)
print('-'*50)
while cont < 9 and c <= 16:
    print(f'{listagem[c]:.<30} R${listagem[c+1]:4.2f}')
    c+=2
print('-'*50)
