"""
Crie uma função que recebe 2 numeros.O primeiro valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo
"""
def aumento(num, percent):

    return num + (num * (percent/100))

au = aumento(50, 10)
print(au)
