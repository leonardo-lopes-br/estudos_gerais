n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1+n2) / 2
situacao = 'REPROVADO'
if media >= 7:
    situacao = 'APROVADO'
elif 5 <= media <= 6.9:
    situacao = 'RECUPERAÇÃO'
print(f'Situação do aluno: {situacao}')
