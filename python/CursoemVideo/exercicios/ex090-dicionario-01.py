situacao = {
    'Nome': str(input('Nome: ')),
    'Média': float(input('Média: ')),
    'Situação': ' '
    }
print('-'*15)
if situacao['Média'] < 5:
    situacao['Situação'] = 'REPROVADO'
elif situacao['Média'] < 7: 
    situacao['Situação'] = 'RECUPERAÇÃO'
else:
    situacao['Situação'] = 'APROVADO'
for k, v in situacao.items():
    print(f'{k}: {v}')
