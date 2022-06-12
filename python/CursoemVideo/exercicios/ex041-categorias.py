from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
categoria = 'MIRIM'
if idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <=19:
    categoria = 'JUNIOR'
elif idade == 20:
    categoria = 'SÊNIOR'
elif idade > 20:
    categoria = 'MASTER'
print('Categoria do atleta: {}'.format(categoria))