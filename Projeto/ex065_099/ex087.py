#ex087.py

carrinho = []
carrinho.append(('prod1', 30))
carrinho.append(('prod2', 45))
carrinho.append(('prod3', 22))
carrinho.append(('prod4', 93))
carrinho.append(('prod5', 6))

total = 0 

for produtos in carrinho:
    total = total + produtos[1]

print(f'O total é de: R$ {total}')


for x,y in carrinho:
    total = total + y 