expressao = str(input('Digite a expressão: '))
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão está Correta! Parabéns!')
else:
    print('Sua expressão está Incorreta! Verifique os parênteses!')
