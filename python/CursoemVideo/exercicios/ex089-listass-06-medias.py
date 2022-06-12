alunos = []
alunos2 = []
mais = pergunta = ' '
while True:
    while mais != 'N':
        nome = str(input('Nome: '))
        n1 = float(input('1ª Nota: '))
        n2 = float(input('2ª nota: '))
        alunos2.append(nome)
        alunos2.append(n1)
        alunos2.append(n2)
        alunos.append(alunos2[:])
        alunos2.clear()
        mais = str(input('Adicionar mais alunos [S/N]: ')).strip().upper()[0]
        while mais not in 'SN':
            mais = str(input('Adicionar mais alunos [S/N]: ')).strip().upper()[0]
    print('-='*4 + ' BOLETIM DOS ALUNOS ' + '-='*4)
    for a in range(0,len(alunos)):
        print(f'Aluno(a) {a+1}: {alunos[a][0]}; Média: {(alunos[a][1] + alunos[a][2])/2}')
    print('-='*18)
    break
flag = 0
while flag != 999:
    flag = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if 1 <= flag <= len(alunos): 
        print(f'Notas de {alunos[flag-1][0]} são {alunos[flag-1][1]} e {alunos[flag-1][2]}')
        print('-'*40)
    else:
        if flag != 999:
            print('Aluno inexistente!')
            print('-'*40)
print('FINALIZANDO....\nVolte sempre!')
