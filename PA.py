x = int(input('digite o primeiro termo da P.A'))
y = int(input('digite a razao da P.A'))
z = x + (10 - 1) * y
for c in range(x, z + y, y):
    print('{}'.format(c))