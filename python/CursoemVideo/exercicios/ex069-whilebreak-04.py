cont = 1
maiores = homens = mulheres20 = 0
while True:
    idade = int(input('Idade da {}ª pessoa: '.format(cont)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]: '.format(cont))).strip().upper()[0]
    cont += 1
    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        if sexo == 'F' and idade < 20:
            mulheres20 += 1
        if idade >= 18:
            maiores += 1
        if sexo == 'M':
            homens += 1
        break
    elif pergunta == 'S':
        if sexo == 'F' and idade < 20:
            mulheres20 += 1
        if idade >= 18:
            maiores += 1
        if sexo == 'M':
            homens += 1
    else:
        print('Erro! Tente novamente!')
        cont -= 1
print('Ao todo {} pessoa(s) cadastrada(s) são MAIORES'.format(maiores))
print('Ao todo {} mulher(es) cadastrada(s) tem MENOS de 20 anos'.format(mulheres20))
print('Ao todo {} HOMEM(NS) foram cadastrado(s)'.format(homens))
