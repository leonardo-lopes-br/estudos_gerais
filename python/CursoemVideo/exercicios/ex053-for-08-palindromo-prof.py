frase = str(input('Digite um texto: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # ou seja do começo ao fim, de trás pra frente
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('O texto digitado não é um Palíndromo!')