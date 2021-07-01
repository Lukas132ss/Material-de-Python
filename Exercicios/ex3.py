"""
Faça um programa que peça o primeiro o nome do usuário
Se o nome tiver quatro ou menos letras escreva 'seu nome é curto'
Se o nome tiver entre 5 e 6 letras escreva 'seu nome é normal'
Maior que 6 escreva 'seu nome é muito grande'
"""
nome = input('Digite seu primeiro nome: ')
nome = len(nome)


if nome <= 4:
    print('Seu nome é curto.')

elif nome == 5 or nome == 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande.')