v = int(input('Qual o valor a ser sacado? '))
c50 = c20 = c10 = c1 = 0
while True:
    if (v / 50) >= 1:
        c50 = v//50
        v = v - c50*50
        if (v / 20) >= 1:
            c20 = v//20
            v = v - c20*20
            if (v / 10) >= 1:
                c10 = v//10
                v = v - c10*10
                if (v / 1) >= 1:
                    c1 = v//1
                    v = v - c1*1
                    break
print('''Serão:
{} notas de R$50.00
{} notas de R$20.00
{} notas de R$10.00
{} notas de R$1.00'''.format(c50,c20,c10,c1))
