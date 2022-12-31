v = int(input('Digite o termo para calcular a sequencia de fibonacci'))
v1 = 0
v2 = 1
a1 = 2
print(f'{v1}->{v2}', end='')

while a1 != v:
    v3 = v1 + v2
    print('->{}'.format(v3), end='')
    a1 += 1
    v1 = v2
    v2 = v3
