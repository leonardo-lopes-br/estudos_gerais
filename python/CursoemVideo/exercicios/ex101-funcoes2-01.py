def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade < 65:
        condicao = f'Com {idade} anos, o voto é OBRIGATÓRIO!'
    elif 16 <= idade < 18 or idade >= 65: 
        condicao = f'Com {idade} anos, o voto é OPCIONAL!'
    else:
        condicao = f'Com {idade} anos, NÃO VOTA!'
    return condicao
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
