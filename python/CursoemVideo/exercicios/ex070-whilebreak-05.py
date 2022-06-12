print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)
produtos = []
precos = []
continuar = ''
total = cont1 = cont2 = caro = 0
while continuar != 'N':
    produtos.append(input('Nome do produto: '))
    precos.append(float(input('Preço do produto: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if precos[cont1] > 1000:
        caro += 1
    total += precos[cont1]
    cont1 += 1
barato = precos[0]
for c in range(0, len(precos)):
    if barato > precos[c]:
        barato = precos[c]
        cont2 = c
print(f'Sua lista de compras foi: {produtos}')
print(f'O total a pagar é: R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais BARATO foi {produtos[cont2]} que custou R${barato}')
