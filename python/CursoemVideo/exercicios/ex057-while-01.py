sexo = 'g'
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':
        print('\nValor inválido!')
    if sexo == 'M':
        print('Sexo MASCULINO reconhecido!')
    if sexo == 'F':
        print('Sexo FEMININO reconhecido!')
