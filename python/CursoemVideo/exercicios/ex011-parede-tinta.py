largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
area = largura*altura
print('A quantidade de tinta necessária será de {:.2f}L'.format(area/2))

#Visto que cada litro de tinta pinta 2m²
