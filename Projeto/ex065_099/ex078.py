#ex078.py
""" Escreva um programa que recebe um texto do usuário e o converte para código
morse, exibindo em tela o texto em formato Morse, segundo a padronização
'.-' (Ponto, traço) """

texto = input('Digite o texto sem acentos: ').upper()
morse = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 
            'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·','O': '---',
            'P': '·--·','Q': '--·-','R': '·-·','S': '···','T': '-','U': '··-','V': '···-','W': '·--','X': '-··-','Y': '-·--',
            'Z': '--··', ' ': ' '}

for i in range(0, len(texto)):
    print(morse.get(texto[i]), end='')