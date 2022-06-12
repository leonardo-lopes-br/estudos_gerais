p1 = float(input('Digite o primeiro termo da PA: '))
p1_copia = p1
r = float(input('Digite a razão da PA: '))
print('\nOs 10 primeiros termos da PA formada são:', end = ' ')
while True:
    print(p1, end = ' ')
    p1 += r
    if p1 == p1_copia + 10*r:
        break
