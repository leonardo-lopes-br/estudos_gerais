pergunta = ''
n = int(input('Digite um valor: '))
maior = menor = soma = n
cont = 1
while True:
    pergunta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    if pergunta not in 'sn':
        print('Resposta inválida!')
    elif pergunta == 's':
        n = int(input('Digite um valor: '))
        cont += 1
        soma += n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    elif pergunta == 'n':
        break
print('A média dos {} valores digitados é {}, o maior valor é {} e o menor valor é {}'.format(cont,soma/cont,maior,menor))
