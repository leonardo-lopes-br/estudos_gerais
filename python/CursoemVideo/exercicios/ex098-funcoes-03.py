from time import sleep
def contador(início,fim,passo):
    if passo == 0 and início > fim:
        for cont in range(início,fim-1,-1):
            print(f'{cont}', end = ' ',flush=True) # o flush faz com que o sleep funcione antes da finalização da função
            sleep(0.5)
    elif passo == 0 and início < fim:
        for cont in range(início,fim+1,1):
            print(f'{cont}', end = ' ',flush=True)
            sleep(0.5)
    if início < fim and passo != 0:
        for cont in range(início,fim+1,passo):
            print(f'{cont}', end = ' ',flush=True)
            sleep(0.5)
    elif início > fim and passo != 0:
        if passo > 0:
            for cont in range(início,fim-1,-passo):
                print(f'{cont}', end = ' ',flush=True)
                sleep(0.5)
        elif passo < 0:
            for cont in range(início,fim-1,passo):
                print(f'{cont}', end = ' ', flush=True)
                sleep(0.5)
print('Contagem de 1 a 10:')
contador(1,10,1)
print('\nContagem de 10 a 0, de 2 em 2:')
contador(10,-1,-2)
print()
print('-='*20)
print('Contagem personalizada:')
inicio_usuario = int(input('Início: '))
fim_usuario = int(input('Fim: '))
passo_usuario = int(input('Passo: '))
contador(inicio_usuario,fim_usuario,passo_usuario)
print()
print('-='*20)
