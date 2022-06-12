peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/(altura**2)
condicao = ''
if imc < 18.5:
    condicao = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    condicao = 'Peso Ideal'
elif 25 <= imc < 30:
    condicao = 'Sobrepeso'
elif 30 <= imc < 40:
    condicao = 'Obesidade'
else:
    condicao = 'Obesidade Mórbida'
print(f'Status: {condicao}')