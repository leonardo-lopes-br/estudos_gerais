palavras = ('Leonardo','Marcela','Lauren','Matheus','Gabriel','Guilherme','Lucas','Pedro','Elisangela','Tereza','Juan','Rafael')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
#Aprender a usar esse estilo de for (porque ele é muito bom)
