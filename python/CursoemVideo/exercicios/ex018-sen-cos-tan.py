from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O seno do ângulo {angulo} é: {seno:.2f}')
print(f'O cosseno do ângulo {angulo} é: {cosseno:.2f}')
print(f'A tangente do ângulo {angulo} é: {tangente:.2f}')

#RADIANS serve pra converter de graus pra radianos, porque as funções seno, cosseno e tangente recebem valores em radianos
