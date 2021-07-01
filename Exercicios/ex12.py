"""
Crie uma função1 que recebe uma função2 como parametro e retorne o valor da funcao2 executada
Faça a funcao1 executar as duas funcões que recebam um numero diferente de argumentos
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome} '
def saudacao(saudacao, nome):
    return f'{saudacao} {nome}'

exec = mestre(fala_oi, 'Lukas')
print(exec)
exec2 = mestre(saudacao,'Bom dia!', 'Lukas')
print(exec2)

