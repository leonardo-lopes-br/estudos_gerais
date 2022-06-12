velocidade = float(input('Velocidade do carro: '))
if velocidade > 80:
    print('MULTADO! Você deverá pagar: R${:.2f}'.format((velocidade-80)*7))
print('Dirija com cuidado e utilize o cinto de segurança!')