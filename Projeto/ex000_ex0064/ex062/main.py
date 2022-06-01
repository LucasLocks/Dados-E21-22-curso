#Arquivo main.py

import medicos
import cadastro_plano_saude

usuario =str(input('Digite seu número de usuário: '))
if usuario in cadastro_plano_saude.keys():
    if usuario == '001':
        usuario = 'Adriano'
    if usuario == '002':
        usuario = 'Karina'
        print('Bem vindo(a)', usuario)
    else:
        print('Usuario não cadastrado!')

menu = str(input('Deseja agendar uma consulta? (S ou N): ')).upper().strip()

if menu == 'S':
    paciente = input('Por favor digite seu nome: ')
    print(f'{paciente}, escolha qual médico deseja consultar:')
    print('1-Dr Pimpolho')
    print("2 -Dra Zileide")
    medico = int(input("Com qual médico deseja consultar? "))
    if medico == 1:
        print(f'Sua consulta com o {medicos.medicos[0]} será agendada.')

    if medico == 2:
        print(f'Sua consulta com a {medicos.medicos[1]} será agendada.')

else:
    print('Agradecemos o seu contato !')
