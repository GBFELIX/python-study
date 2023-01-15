x = list()
p = list()
i = list()
y = int(input('digite quantos numeros deseja adicionar'))
for c in range(y):
    a = int(input('digite um numero'))
    x.append(a)
    if a % 2 == 0:
        p.append(a)
    else:
        i.append(a)
print(f' A lista de numeros pares contem os seguintes numeros {p}, ja a lista de numeros impares contem {i}. todos os valores digitados são {x}')

