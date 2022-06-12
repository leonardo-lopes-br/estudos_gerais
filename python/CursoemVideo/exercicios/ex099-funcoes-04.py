from time import sleep
def maior(*num):
    if len(num) > 0:
        maior = num[0]
        print('Valores analisados:', end = ' ')
        for i in range(0,len(num)):
            if  num[i] > maior:
                maior = num[i]
            print(f'{num[i]}', end = ' ', flush=True)
            sleep(0.5)
        print()
        print(f'Foram informados {len(num)} valores')
        print(f'Maior: {maior}')
    else:
        print(f'Foram informados {len(num)} valores')
        print(f'Maior: 0')
        
maior(3,43,55,790,33,-21,0,33,25)
maior()
maior(0,0,0)
