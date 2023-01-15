x = int(input('digite o ano de nascimento'))
y = int(input('digite o ano atual'))
z = y - x
if z > 18:
    a = z - 18
    print('O tempo de se alistar ja passou em {} anos'.format(a))
elif z < 18:
    b = (x - y) + 18
    print('Ainda falta {} anos para se alistar'.format(b))
elif z == 18:
    print('Você deve se alistar esse ano')