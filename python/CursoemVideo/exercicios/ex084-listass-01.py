pessoas = []
listaAux = []
pesados = []
leves = []
pergunta = ' '
cont = pesado = leve = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    listaAux.append(nome)
    listaAux.append(peso)
    pessoas.append(listaAux[:])
    if peso > pesado:
        pesado = peso
    if len(pessoas) == 2 or peso < leve:
        leve = peso
    cont += 1
    listaAux.clear()
    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta not in 'SN':
        while pergunta not in 'SN':
            pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
for elemento in pessoas:
    if elemento[1] == pesado:
        pesados.append(elemento[0])
    if elemento[1] == leve:
        leves.append(elemento[0])
print(f'Foi/Foram cadastrado(as) {cont} pessoa(s)')
print(f'A(s) pessoa(s) mais pesada(s) [{pesado}] foi/foram {pesados}')
print(f'A(s) pessoa(s) mais leve(s) [{leve}] foi/foram {leves}')
