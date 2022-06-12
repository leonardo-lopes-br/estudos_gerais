n = int(input('Digite um número inteiro: '))
print("""\nConversão do Número\n\n
         [1] BINÁRIO
         [2] OCTAL
         [3] HEXADECIMAL""")
opcao = int(input('\nDigite o índice de sua conversão: '))
if opcao == 1:
    print('O valor {} convertido de inteiro para BINÁRIO é: {}'.format(n,bin(n)[2:])) #o [2:] aqui em cada um é porque aparece o tipo da base antes do numero (0b pra binario, 0o para octal e 0x para hexadecimal)
elif opcao == 2:
    print('O valor {} convertido de inteiro para OCTAL é: {}'.format(n,oct(n)[2:]))
elif opcao == 3:
    print('O valor {} convertido de inteiro para HEXADECIMAL é: {}'.format(n,hex(n)[2:]))
else:
    print('Valor inválido!')