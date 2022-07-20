#ex061b.py

def ela_mesma(n):
    if n <= 1:
        return n
    else:
        return ela_mesma(n-1) + ela_mesma(n-2)

num = int(input('Digite um número: '))

resposta = ela_mesma(num-1)
print(resposta)
