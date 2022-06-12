p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = []
cont1 = cont2 = contador = 0
mais = -1
while True:
    pa.append(p1 + cont1)
    cont1 += r
    if len(pa) == 10:
        print(f'PA: {pa}')
        break
mais = int(input('Adicionar: '))
while True:
    if mais == 0:
        break
    else:
        cont2 = r
        pa.append(pa[len(pa)-1] + cont2)
        cont2 += r
        contador += 1
    if contador == mais:
        print(f'PA: {pa}')
        mais = int(input('Adicionar: '))
        contador = 0
print('\nPA finalizada!')
# ESSE DEU TRAMPO HEIN PUTA QUE PARIU