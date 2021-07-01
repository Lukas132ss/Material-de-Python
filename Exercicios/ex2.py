"""
Faça um programa que pergunte a hora ao usuário e de acordo com o horário
exiba uma saudação apropriada.
"""
hora = input('Digite o horário(0-23): ')
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('O horario deve ser entre 0 e 23.')
    else:
        if hora <= 11:
            print('Bom dia')
        elif hora >= 12 and hora <= 17:
            print('Boa tarde')
        elif hora >=18 and hora <=23:
            print('Boa noite')

else:
    print('Você não digitou um número.')
