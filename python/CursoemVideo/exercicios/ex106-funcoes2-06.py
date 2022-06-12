from time import sleep
def linha(msg):
    print(f'~'*(len(msg)+4))
    print(f'  {msg}')
    print(f'~'*(len(msg)+4))


def menu(comando):
    while True:
        menu = '\33[0;30;42mSISTEMA DE AJUDA PYHELP\033[m'
        linha(menu)
        opcao = str(input('Função ou biblioteca: '))
        if opcao == 'fim':
            break
        acesso = f"Acessando o manual do comando '{opcao}'"
        linha(acesso)
        sleep(1)
        help(opcao)
    linha('Até Logo!')
menu(input)
