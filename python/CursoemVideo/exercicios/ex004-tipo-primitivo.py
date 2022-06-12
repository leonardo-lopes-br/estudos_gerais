algo = input('Digite uma sentença (pode incluir números): ')
print('O tipo primitivo da sentença digitada é:',type(algo)) #mostra o tipo primitivo da variável
print('A sentença digitada é numérica? ',algo.isnumeric()) #verifica se o conteudo da variavel pode ser convertido em numérico
print('A sentença digitada é alfabética? ',algo.isalpha()) #verifica se o conteudo da variavel é alfabetico
print('A sentença digitada é alfanumérica? ',algo.isalnum()) #verifica se o conteudo é alfanumerico
print('A sentença só tem espaçoes? ', algo.isspace()) #verifica se contem apenas espaços
print('Está em maiúsculas? ', algo.isupper()) #verifica se está tudo em maiusculo
print('Está em minúsculas? ', algo.islower()) #verifica se está tudo em minusculo
print('Está capitalizada? ', algo.istitle()) #verifica se está formatado como um titulo/nome proprio (primeira letra maiuscula apenas)

# TODAS AS VARIÁVEIS NO PYTHON SÃO OBJETOS
# AQUI POR EXEMPLO, TEMOS VARIOS METODOS RELACIONADOS AO OBJETO DO TIPO STRING (isupper,isnumeric, etc)