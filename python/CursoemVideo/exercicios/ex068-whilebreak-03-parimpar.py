from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
pc = randint(0,10)
cont = 0
parimpar = ''
venceu = False
while True:
    n = int(input('Digite um valor: '))
    decisao = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    if decisao == 'I':
        if (n+pc) % 2 == 0:
            parimpar = 'PAR'
        else:
            parimpar = 'IMPAR'
        print('\nVocê jogou {} e o computador jogou {}. Total de {}, deu {}'.format(n,pc,n+pc,parimpar))
        if parimpar == 'IMPAR':
            venceu = True
            cont +=1
            print('\nVocê VENCEU! Vamos jogar mais uma vez....')
        else:
            break
    elif decisao == 'P':
        if (n+pc) % 2 == 0:
            parimpar = 'PAR'
        else:
            parimpar = 'IMPAR'
        print('\nVocê jogou {} e o computador jogou {}. Total de {}, deu {}'.format(n,pc,n+pc,parimpar))
        if parimpar == 'PAR':
            venceu = True
            cont +=1
            print('\nVocê VENCEU! Vamos jogar mais uma vez....')
        else:
            break
    else:
        print('Erro! Tente Novamente!')
print('-'*60)
print(f'\nGAME OVER, Você venceu {cont} vezes')
