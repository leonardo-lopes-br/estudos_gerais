nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()
print(f'Primeiro nome: {nome_separado[0]}')
print(f'Último nome: {nome_separado[len(nome_separado)-1]}')