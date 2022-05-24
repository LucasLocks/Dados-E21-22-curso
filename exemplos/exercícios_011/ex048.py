# ex048.py
"""
Crie um sistema de perguntas e respostas que interage com o usuário, pedindo que
o mesmo insira uma resposta. Caso a primeira questão esteja correta, exiba em 
tela uma mensagem de acerto e para para a proxima pergunta, caso incorreta,
exiba uma mensagem de erro e pule para a proxima pergunta. Dicts. 
"""
from ex048base import base

respostas_certas = 0 

for pkeys,pvalues in base.items():
    print(f'{pkeys}:{pvalues["pergunta"]}')

    for rkeys,rvalues in pvalues['alternativas'].items():
        print(f'[{rkeys}]:{rvalues}')

    resposta = input('\nEscolha uma alternativa: [a],[b],[c], ou [d]: ')
    print('')
    if resposta == pvalues['resposta_certa']:
        print('Resposta Correta!!!')
        respostas_certas += 1
    else:
        print('Resposta ERRADA')

if respostas_certas == 0:
    print('Voce não acertou nenhuma questão!')
elif respostas_certas == 1:
    print('Você acertou apenas uma questão')
else: 
    print(f'Você acertou {respostas_certas}. Parabéns!!!!')