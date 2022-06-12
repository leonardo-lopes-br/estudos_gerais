from datetime import date
maioridade = 0
juvenil = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - ano >= 21:
        maioridade += 1
    else:
        juvenil += 1
print('\nDas 7 pessoas cadastradas, temos:')
print(f'- {maioridade} pessoas que JÁ atingiram a MAIORIDADE')
print(f'- {juvenil} pessoas que AINDA NÃO atingiram a MAIORIDADE')
    