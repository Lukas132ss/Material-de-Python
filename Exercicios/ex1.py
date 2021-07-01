"""
Faça um usuário digitar um número inteiro
Informe se esse número é par ou impar
Informe o usuário caso não seja um número inteiro
"""

num_1 = (input('Digite outro inteiro: '))
if num_1.isdigit():
    num_1 = int(num_1)
    par = num_1 % 2

    if par == 0:
        print(f'{num_1} é par')
    else:
        print(f'{num_1} é impar')

else:
    print('Esse número não é inteiro')
