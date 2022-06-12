from datetime import date
ano = int(input('Digite um ano (se quiser analisar o ano atual, digite 0): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É um ano bissexto!')
else:
    print(f'O ano {ano} NÃO É um ano bissexto!')
       