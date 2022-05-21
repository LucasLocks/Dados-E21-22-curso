# ex047c.py

data = {
    'faltas' : [],
    'notas': []
}
data['notas'].append('10')
data['notas'].append('20')
data['notas'].append('30')
data['faltas'].append('12')
print(data)
print(type(data))
print(data['faltas'])
print(type(data['faltas']))
print(data['notas'])
print(type(data['notas']))

n = data['notas']

for i in range(0,len(n),1):
    print(n[i])

for i in n:
    print(i)



