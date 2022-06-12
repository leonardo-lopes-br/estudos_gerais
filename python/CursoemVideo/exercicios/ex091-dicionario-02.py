from random import randint
from time import sleep
from operator import itemgetter # aparentemente utilizado para ordenar um dicionario em outro (dentre outras funções)
colocacao = []
jogadores = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)}
ranking = []
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.6)
print('Ranking dos Jogadores:')
sleep(0.6)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) #colocando um dicionário ordenado dentro de outro com o sorted pra colocar em ordem e o itemgetter para escolar no dicionario qual chave vai ser colocada em ordem (como no parentes é 1, está ordenando pelo valor das chaves)
cont = 1
for i in range(0,len(ranking)):
    print(f'{cont}º lugar: {ranking[i][0]} com {ranking[i][1]}')
    cont +=1