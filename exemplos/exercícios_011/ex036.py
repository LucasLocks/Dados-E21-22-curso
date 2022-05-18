#ex036.py
#Crie um programa que pede ao usuário uma frase ou palavra, verifique se a frase é palíndromo ou não. E exiba o resultado. : A base do teto desaba. A cara rajada da jararaca. Acuda cadela da Leda caduca. A dama admirou o rim da amada. A Daniela ama a lei? Nada! Adias a data da saída. A diva em Argel alegra-me a vida. A droga do dote é todo da gorda. https://www.todamateria.com.br/palindromo/

frase = str(input('Digite uma palavra ou frase: ')).strip().upper()

palavras = frase.split()
print(palavras)

caracteres = ''.join(palavras)
print(caracteres)

fraseinvertida = ''

#range(inicio, fim, passo)
for i in range(len(caracteres)-1,-1,-1):
    fraseinvertida += caracteres[i]

print(caracteres,fraseinvertida)
if fraseinvertida == caracteres:
    print('É um palíndromo !')
else:
    print('Não é palíndromo !')