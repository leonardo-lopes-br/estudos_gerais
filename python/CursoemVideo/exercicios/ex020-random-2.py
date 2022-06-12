import random

a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

lista = [a1,a2,a3,a4]
#random.shuffle(lista)   UM dos métodos
ordem = random.sample(lista,3)
print('A ordem de apresentação será:\n')
print(ordem)

# O metódo shuffle embaralha os elementos de uma lista
# O sample é o mesmo que o shuffle, mas voce pode escolher a quantidade de elementos da lista a serem escolhidos
# Alem disso o SAMPLE precisa ser armazenado em uma variável
# O choices é parecido com o sample, mas ele permite escolher um mesmo elemento DUAS ou mais vezes