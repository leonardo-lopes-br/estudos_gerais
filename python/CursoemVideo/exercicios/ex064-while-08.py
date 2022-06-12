n = cont = soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para sair]: '))
    if n != 999:
        cont += 1
        soma += n
print('Você digitou {} números, e a soma entre eles é {}'.format(cont,soma))
