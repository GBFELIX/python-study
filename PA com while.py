a = int(input('Primeiro termo da PA: ').strip())
b = int(input('Razão da PA: ').strip())
c = a
print('{}, '.format(a), end='')
while a != c + 9 * b:
    a += b
    print('{}, '.format(a), end='')


