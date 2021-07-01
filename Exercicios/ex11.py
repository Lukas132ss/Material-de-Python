"""
Crie uma função1 que recebe uma função2 como parametro e retorne o valor da funcao2 executada
"""

def func1():
    return 'Olá mundo'

def mestre(funcao):
    return funcao()

exec = mestre(func1)
print(exec)