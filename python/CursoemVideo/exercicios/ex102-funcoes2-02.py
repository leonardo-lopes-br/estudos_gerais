def fatorial(n,show=False):
    """
     => Calcula o fatorial de um número
     parametro n: numero a calcular o fatorial
     parametro show (opcional): mostra toda a conta que foi feita
    """
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f'{n}! = ', end = '')
    if show:
        for j in range(n,0,-1):
            if j == 1:
                print(f'{j} = ', end = '')
            else:
                print(f'{j} x ', end = '')
        print(f'{f}')
        print()
    else:
        print(f'{f}')
fatorial(6,True)
help(fatorial)
