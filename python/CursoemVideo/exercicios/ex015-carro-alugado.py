km = int(input('Quantos km rodados? '))
dias = int(input('Alugado por quantos dias? '))
pagar = 60*dias + 0.15*km
print('Você deverá pagar R${:.2f}'.format(pagar))

#Aqui o preço calculado a pagar é tal sabendo que cada quilômetro custa R$0,15 e cada dia R$60,00