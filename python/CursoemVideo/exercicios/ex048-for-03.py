soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma entre todos os {} números ímpares E divisíveis por 3 é: {}'.format(cont,soma))

#numeros entre 1 e 500 impares e divisiveis por 3
    