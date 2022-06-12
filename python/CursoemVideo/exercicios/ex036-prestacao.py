valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
prazo_anos = int(input('Anos: '))
prestacao = valor_casa / (prazo_anos*12)
if prestacao <= 0.3*salario:
    print('EMPRESTIMO ACEITO! Sua prestação será de R${:.2f}'.format(prestacao))
else:
    print('EMPRESTIMO NEGADO!')


