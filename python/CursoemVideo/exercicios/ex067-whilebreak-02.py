while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    else:
        cont = -1
        print('-'*15)
        while True:
            cont += 1
            print(f'{n} x {cont:2} = {n*cont}')
            if cont == 10:
                break
        print('-'*15)
print('\nPROGRAMA TABUADA ENCERRADO. Volte sempre!')
