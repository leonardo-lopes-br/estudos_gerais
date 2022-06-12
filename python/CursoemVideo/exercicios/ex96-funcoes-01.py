def área(l,c):
    area = l*c
    print(f'A área de um terreno {l:.2f} x {c:.2f} é de {area:.2f} m².')
print(' Controle de terrenos')
print('-'*25)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura,comprimento)
