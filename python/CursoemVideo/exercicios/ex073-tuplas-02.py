times = ('Fortaleza','Athletico-PR','Atlético GO','Bragantino','Bahia','Fluminense','Palmeiras','Flamengo',
         'Atlético MG','Corinthians','Ceará SC','Santos','Cuiabá','Sport Recife','São Paulo','Juventude','Internacional',
         'Grêmio','América MG','Chapecoense')
print('Times do Brasileirão: {}'.format(times))
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição')
