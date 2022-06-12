l1 = int(input('1º lado do triângulo: '))
l2 = int(input('2º lado do triângulo: '))
l3 = int(input('3º lado do triângulo: '))
triangulo = 'ISÓSCELES'
if l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    if l1 != l2 and l2 != l3 and l3 != l1:
        triangulo = 'ESCALENO'
    elif l1 == l2 == l3:
        triangulo = 'EQUILÁTERO'
    print(f'O triângulo formado com estas medidas é {triangulo}')
else:
    print('As medidas NÃO formam um triângulo!')
