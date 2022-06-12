salario = float(input('Digite seu salário: '))
if salario <= 1250:
    print(f'Você receberá um aumento de 15%, portanto, seu novo salário será de R${salario*1.15:.2f}')
else:
    print(f'Você receberá um aumento de 10%, portanto, seu novo salário será de R${salario*1.1:.2f}')