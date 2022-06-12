'''
- len(frase) retorna o tamanho de uma string por exemplo (len é de length)

- frase.count('o',0,13) retorna quantos caracteres indicados tem na string, podendo ter os parametros de inicio e fim ali tbm (0 a 13 aqui)

- frase[0:7:2] pega do começo da string (indice 0) vai até o indice 7 e pulando de 2 em 2 (o indice de strings começa em 0)
   no caso acima ele vai ignorar a posição 7, ele apenas para quando chega nela e n contabiliza
   
- frase.find('deo') vai retornar a primeira posição onde o "deo" começa na string
   se o find retornar o valor -1 significa que esse conjunto de caracteres não existe na string
   
- 'palavra' in frase -> vai retornar true ou false conforme a presença ou não do conjunto de caracteres na string frase

- frase.replace('palavra2','palavra1') esse método vai substituir uma palavra dentro da string (1º paramentro) por outra (2º parametro)
   essa configuração não vai ficar salva a menos que vc armazene na propria variavel: frase = frase.replace('palavra2','palavra1')

- frase.upper() coloca tudo em maiusculas

- frase.lower() coloca tudo em minusculas

- frase.capitalize() coloca a primeira letra em maiuscula e o resto em minuscula

- frase.title() coloca a primeira letra de todas as palavras da string em maiuscula e o resto minuscula (reconhece palavras por espaços)

- frase.strip() vai remover espaços inuteis no começo e no final da string

- frase.rstrip() vai remover os espaços inuteis apenas do final (right = direita)

- frase.lstrip() vai remover os espaços inuteis apenas no começo (left = esquerda)

- frase.split() vai dividir a string em varias strings menores, quebradas pelos espaços (split = dividir)
   nesse caso as novas palavras terão seus indices proprios e será gerada uma lista em que cada palavra inteira será um indice
   
- '-'.join(frase) vai juntar as palavras divididas pelo split, separando elas pela string digitada antes do join

- para criar um print longo que ocupe varias linhas voce pode usar """ (tres aspas duplas) ex: print(""" kjdkbkdsbjks """)

- comentarios de uma linha no python são com # e com varias são com tres aspas simples