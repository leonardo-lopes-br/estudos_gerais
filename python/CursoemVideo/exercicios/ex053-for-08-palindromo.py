frase = str(input('Digite uma frase: ')).strip().upper()
ehPalindromo = False
normal = ''
inversa = ''
for c in range(0,len(frase)):
    if frase[c] != ' ':
        normal += frase[c]
for j in range(len(frase)-1,-1,-1):
    if frase[j] != ' ':
        inversa += frase[j]
print('O texto {} ao contrário é {}'.format(normal,inversa))
if normal == inversa:
    ehPalindromo = True
    print('Portanto, o texto É UM PALÍNDROMO!') 
else:
    print('O texto NÃO É UM PALÍNDROMO!')
#minha solução