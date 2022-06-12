def leiaInt(b):
    try:
        c = input(b)
    except KeyboardInterrupt:
        print('Usuário preferiu não informar os dados')
    '''if c.isnumeric() == True:
        c = int(c)
    else:
        while True:
            print('\033[0;31;40m ERRO! Digite um número válido!\033[m')
            c = input(b)
            if c.isnumeric() == True:
                c = int(c)
                break
    return c'''


def leiaFloat(num):
    d = input(num)
    if d.isnumeric() == True:
        d = float(d)
    else:
        while True:
            print('\033[0;31;40m ERRO! Digite um número válido!\033[m')
            d = input(num)
            if d.isnumeric() == True:
                d = float(d)
                break
    return d

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1} e o número real {n2}')
