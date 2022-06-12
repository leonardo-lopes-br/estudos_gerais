n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
flag = 0
while flag != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    flag = int(input('Operação desejada: '))
    if flag == 1:
        soma = n1+n2
        print('\nSoma: {} + {} = {}'.format(n1,n2,soma))
    elif flag == 2:
        multi = n1*n2
        print('\nMultiplicação: {} x {} = {}'.format(n1,n2,multi))
    elif flag == 3:
        if n1 >= n2:
            maior = n1
        else:
            maior = n2
        print('Entre os números, o maior é {}'.format(maior))
    elif flag == 4:
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
    else:
        if flag != 5:
            print('\nValor inválido! Digite uma operação!')
print('\n' + '-='*7 + ' PROGRAMA FINALIZADO ' + '-='*7)
