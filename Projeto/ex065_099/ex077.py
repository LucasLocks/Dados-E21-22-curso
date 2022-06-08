#ex077.py
""" Defina uma função que pode aceitar duas string como entrada, exibindo em
tela apenas a string de maior tamanho/comprimento. Caso as duas string tenham
mesmo tamanho exiba as duas. """

frase1 = input ("Digite a 1° frase ou palavra: ")
frase2 = input ("Digite a 2° frase ou palavra:: ")
   
tamf1 = (len(frase1))
tamf2 = (len(frase2))
 
if tamf1>tamf2:
    print ('frase1 é maior que frase2')
elif tamf1<tamf2:
    print ('frase2 é maior que frase1')  

else:
    print ('frase 1 é do mesmo tamanho que frase 2')