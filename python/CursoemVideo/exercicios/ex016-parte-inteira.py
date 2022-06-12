from math import floor as arredondarprabaixo

n = float(input('Digite um número: '))
#print(f'A parte inteira do número {n} é {arredondarprabaixo(n)}')  UMA DAS SOLUÇÕES, poderia usar a função trunc
print(f'O número digitado foi {n} e sua parte inteira é: {int(n)}')

#A biblioteca Math tem varias funções da matematica (seno, cosseno, etc)
# Quando importamos com o "from" pra pegar uma função especifica, basta utilizar a função com uma variavel [floor(var)]
# se fosse pegar toda a biblioteca, na hora de usar uma função, teria que ter o nome da biblioteca e um ponto antes da função:
# ex: math.floor(var)
#Usando o "as" vc da um apelido pra função que pegou