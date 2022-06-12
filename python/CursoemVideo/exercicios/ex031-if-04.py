distancia = float(input('Qual a distância da viagem? (KM) '))
if distancia <= 200:
    print(f'O valor da viagem será de R${0.5*distancia:.2f}')
else:
    print(f'O valor da viagem será de R${0.45*distancia:.2f}')