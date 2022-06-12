from random import randint
numbers = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os valores sorteados foram: {}'.format(numbers))
maior = menor = numbers[0]
for num in range(0,len(numbers)):
    if numbers[num] > maior:
        maior = numbers[num]
    if numbers[num] < menor:
        menor = numbers[num]
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
