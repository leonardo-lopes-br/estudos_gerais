import math
co = int(input('Digite o 1º cateto do triângulo retângulo: '))
ca = int(input('Digite o 2º cateto do triângulo retângulo: '))
#h = (co**2 + ca**2)**(1/2)  JEITO MATEMATICO DE FAZER
h = math.hypot(co,ca) #calcula a hipotenusa
print(f'A hipotenusa deste triângulo retângulo seria: {h}')