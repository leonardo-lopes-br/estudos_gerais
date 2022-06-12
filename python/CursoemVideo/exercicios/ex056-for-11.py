soma = 0
homens = []
mulheres = []
maisVelho = 0
homemMaisVelho = ''
for c in range(1,5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).strip().upper()
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}ª pessoa [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo INVÁLIDO!')
        sexo = str(input(f'Digite o sexo da {c}ª pessoa [M/F]: ')).strip().upper()
    if sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            homemMaisVelho = nome
    soma += idade
    if sexo == 'F':
        if idade < 20:
            mulheres.append(nome)
print(f'A média de idade do grupo é de {soma/4} anos')
print(f'O homem mais velho da lista é o {homemMaisVelho.capitalize()}')
print(f'A lista possui {len(mulheres)} mulheres com MENOS de 20 anos')
