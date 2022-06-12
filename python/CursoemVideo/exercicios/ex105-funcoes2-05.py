def notas(*notas,sit = False):
    """
     => Recebe quantas notas forem necessarias de alunos e calcula a media,
     a nota mais alta, a mais baixa, o total de notas e a situação (opcional) e
     armazena tudo em um dicionario
        parametro *notas ===> recebe as notas (quantas necessario) e as coloca em uma tupla
        parametro sit ======> relativo a situação da media dos alunos
        return =============> retorna o dicionario criado
    """
    info = {
        'total': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'média': sum(notas)/len(notas)
    }
    if sit:
        if info['média'] < 5:
            info['situação'] = 'RUIM'
        elif info['média'] < 7:
            info['situação'] = 'RAZOÁVEL'
        else:
            info['situação'] = 'BOA'
    return info

resp = notas(5,3,4,5,6,7,8,9,9,9,5,sit=True)
print(resp)
help(notas)
