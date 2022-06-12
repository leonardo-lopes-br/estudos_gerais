jogador = {'nome': str(input('Nome do Jogador: ')), 'gols': [], 'total': 0}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for j in range(0,partidas):
    gol = int(input(f'Quantos gols na partida {j}? '))
    jogador['total'] += gol
    jogador['gols'].append(gol)
print('-='*50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k in range(0,len(jogador['gols'])):
    print(f'  => Na partida {k}, fez {jogador["gols"][k]} gol(s).')
print(f'Foi um total de {jogador["total"]} gol(s).')
