pessoas = {'nome': ' ', 'sexo': ' ', 'idade': 0}
muitas_pessoas = []
pergunta = ' '
mulheres = []
acimaMedia = []
cont = somaIdade = 0
while pergunta != 'N':
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Idade: '))
    somaIdade += idade
    print('-='*20)
    print('PESSOA CADASTRADA!')
    print('-='*20)
    pessoas['nome'] = nome
    pessoas['sexo'] = sexo
    pessoas['idade'] = idade
    muitas_pessoas.append(pessoas.copy())
    cont += 1
    pergunta = str(input('Cadastrar mais? [S/N]: ')).strip().upper()[0]
    if pergunta not in 'SN':
        while pergunta not in 'SN':
            pergunta = str(input('Cadastrar mais? [S/N]: ')).strip().upper()[0]
    print('-='*20)
for i in range(0,len(muitas_pessoas)):
    if muitas_pessoas[i]['idade'] > somaIdade/cont:
        acimaMedia.append(muitas_pessoas[i]['nome'])
print(f'Foram cadastradas {cont} pessoas!')
print(f'A média entre as idades é de {somaIdade/cont} anos')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'As pessoas com idade acima da média foram: {acimaMedia}')
