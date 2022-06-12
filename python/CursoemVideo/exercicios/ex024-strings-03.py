cidade = str(input('Digite uma cidade: ')).strip()
santo = cidade.split()
tem_santo = 'SANTO' in santo[0].upper()
print(f'Sua cidade começa com Santo? Resposta: {tem_santo}')
