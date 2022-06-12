lado1 = float(input('Digite o comprimento do 1º lado do triângulo: '))
lado2 = float(input('Digite o comprimento do 2º lado do triângulo: '))
lado3 = float(input('Digite o comprimento do 3º lado do triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Estas medidas PODEM formar um triângulo!')
else:
    print('Estas medidas NÃO PODEM formar um triângulo!')