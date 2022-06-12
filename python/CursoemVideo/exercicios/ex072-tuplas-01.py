numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
           'doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
escolha = -1
while not(0 <= escolha <= 20):
    escolha = int(input('Digite um número [0 a 20]: '))
print(f'{escolha} --> {numeros[escolha]}')
