from datetime import date
trabson = {
    'nome': str(input('Nome: ')),
    'idade': int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 não tem): ')),
    }
ano = trabson['idade']
trabson['idade'] = date.today().year - trabson['idade']
for k, v in trabson.items():
    if k == 'ctps':
        if v != 0:
            trabson['contratacao'] = int(input('Ano de contratação: '))
            trabson['salario'] = float(input('Salário: R$'))
            trabson['aposentadoria'] = trabson['idade'] + (35 - (trabson['idade'] - (trabson['contratacao'] - ano))) 
            break
print('-='*40)
for k, v in trabson.items():
    print(f'{k} tem o valor {v}')
