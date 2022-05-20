#ex036e.py

frase = str(input('Digite uma palavra ou frase: ')).strip().upper()

#transforma frase ou palavras em lista
palavras = frase.split()
print(palavras)
print(type(palavras))

#junta todas as palavras
caracteres = ''.join(palavras)
print(caracteres)
print(type(caracteres))