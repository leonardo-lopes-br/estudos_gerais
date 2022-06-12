jogador = {'nome': ' ', 'gols': [], 'total': 0}
jogadores = []
pergunta = ' '
flag = qual = 0
while pergunta != 'N':
    jogador['gols'] = []
    nome = str(input('Nome do Jogador: '))
    jogador['nome'] = nome
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for j in range(0,partidas):
        gol = int(input(f'Quantos gols na partida {j}? '))
        jogador['total'] += gol
        jogador['gols'].append(gol)
    print('-='*35)
    pergunta = str(input('Mais jogadores? [S/N]: ')).strip().upper()[0]
    jogadores.append(jogador.copy())
    jogador['total'] = 0
    if pergunta not in 'SN':
        while pergunta not in 'SN':
            pergunta = str(input('Mais jogadores? [S/N]: ')).strip().upper()[0]
    print('-='*35)
print(f'{"  Cod nome":<10} {"gols":>15} {"total":>20}')
print('-'*50)
for i in range(0,len(jogadores)):
    print(f' {i}   {jogadores[i]["nome"]:<10}{jogadores[i]["gols"]}{jogadores[i]["total"]:>20}')
print('-='*25)
while flag != 999:
    flag = int(input('Mostrar dados de qual jogador? [999 cancela] '))
    if  0 <= flag <= len(jogadores)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[flag]["nome"]}')
        for j in range(0,len(jogadores[flag]['gols'])):
            print(f'No jogo {j} fez {jogadores[flag]["gols"][j]} gol(s)')
    else:
        print(f'ERRO! Não existe jogador com o código {flag}! Tente Novamente!')
print('--- Finalizando...\nVolte sempre!')
