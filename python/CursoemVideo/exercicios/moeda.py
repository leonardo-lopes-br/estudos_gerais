def metade(n,f = False):
    if f:
        m = n/2
        return moeda(m)
    return n/2


def dobro(n,f = False):
    if f:
        m = n*2
        return moeda(m)
    return n*2


def aumentar(n,a,f = False):
    if f:
        m = n + n*(a/100)
        return moeda(m)
    return n + n*(a/100)


def diminuir(n,d,f = False):
    if f:
        m = n - n*(d/100)
        return moeda(m)
    return n - n*(d/100)


def moeda(n):
    return f'R${n:.2f}'


def resumo(p,a,d):
    print('-'*25)
    print('     RESUMO DO VALOR     ')
    print('-'*25)
    print(f'Preço analisado: {moeda(p):>10}')
    print(f'Dobro do preço: {moeda(dobro(p)):>10}')
    print(f'Metade do preço: {moeda(metade(p)):>10}')
    print(f'{a}% de aumento: {moeda(aumentar(p,a))}')
    print(f'{d}% de redução: {moeda(diminuir(p,d))}')
    print('-'*25)

