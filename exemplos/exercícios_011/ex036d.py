#ex036d.py

frase = str(input('Digite uma palavra ou frase: ')).strip().upper()

#transforma frase ou palavras em lista
palavras = frase.split() 

print(palavras)