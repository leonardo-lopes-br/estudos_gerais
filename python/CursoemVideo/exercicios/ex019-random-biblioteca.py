from random import choice
a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

lista = [a1,a2,a3,a4]
sorteado = choice(lista)

print(f'O(a) sorteado(a) foi o(a) {sorteado}')

# O choice pega um elemento aleatorio de uma lista (por exemplo)