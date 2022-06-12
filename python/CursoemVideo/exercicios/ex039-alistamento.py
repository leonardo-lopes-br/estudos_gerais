from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Você ainda vai se alistar no exército! Ainda faltam {} anos'.format(18-idade))
elif idade == 18:
    print('Está na hora do seu alistamento! Aliste-se esse ano!')
else:
    print('Já passou do ano de seu alistamento! Espero que esteja em dia! Você deve ter se alistado há {} anos'.format(idade-18))