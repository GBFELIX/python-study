x = list()
y = int(input('digite quantos numeros deseja adicionar'))
for i in range(y):
    a = int(input('digite um numero'))
    x.append(a)
x.sort(reverse=True)
print(f'Você adicionou {y} valores. {x}', end=' ')
if 5 in x:
    print('O numero 5 foi digitado e faz parte da lista')
else:
    print('O numero 5 não foi digitado e não faz parte da lista')



