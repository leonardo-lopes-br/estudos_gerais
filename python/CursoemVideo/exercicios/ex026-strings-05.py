frase = str(input('Digite uma frase: ')).strip().lower()
letraA = frase.count('a')
posicaoInicial = frase.find('a')
posicaoFinal = frase.rfind('a')
print(f'Sua frase contém {letraA} letra(s) A')
print(f'A sua primeira aparição foi na posição {posicaoInicial + 1}')
print(f'A sua última aparição foi na posição {posicaoFinal + 1}')