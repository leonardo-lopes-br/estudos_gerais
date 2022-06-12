preco = float(input('Preço do produto: R$'))
print('-=-'*20)
print("""\nOPÇÕES DE PAGAMENTO (R${:.2f}):\n
[1]  À VISTA [dinheiro/cheque]: 10% de desconto
[2]  À VISTA [cartão]: 5% de desconto
[3]  2X NO CARTÃO: preço normal
[4]  3X OU MAIS [cartão]: 20% de juros\n""".format(preco))
print('-=-'*20)
print('\n')
opcao = int(input('Forma de pagamento: '))
if opcao == 1:
    print(f'O produto sairá por R${preco*0.9:.2f}')
elif opcao == 2:
    print(f'O produto sairá por R${preco*0.95:.2f}')
elif opcao == 3:
    print(f'O produto sairá por R${preco:.2f}')
elif opcao == 4:
    print(f'O produto sairá por R${preco*1.2:.2f}')
else:
    print('Opção inválida, segue o menu caralho')
