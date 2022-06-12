fibonacci = [0,1]
n = int(input('Quantidade de termos: '))
if n < 0:
    print('Valor inválido!')
elif n == 0:
    print('Vazio')
elif n == 1:
    print('[0]')
elif n == 2:
    print(fibonacci)
else:
    while True:
        fibonacci.append(fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2])
        if len(fibonacci) == n:
            print(fibonacci)
            break
