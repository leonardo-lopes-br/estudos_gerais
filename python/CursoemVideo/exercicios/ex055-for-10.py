maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR peso digitado foi {maior}KG')
print(f'O MENOR peso digitado foi {menor}KG')