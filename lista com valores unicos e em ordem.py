x = list()
y = int(input('digite quantos numeros deseja adicionar'))
for i in range(y):
    a = int(input('digite um numero'))
    if a in x:
        x.remove(a)
    x.append(a)
print(sorted(x))
