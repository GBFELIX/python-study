x = int(input('digite o tamando de a'))
y = int(input('digite o tamando de b'))
z = int(input('digite o tamando de c'))

if y + z > x and x + z > y and x + y > z:

    print('As 3 retas conseguem formar um triangulo')
    if x == y == z:
        print('equilatero')
    elif x != y != z:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('As 3 retas nao conseguem formar um triangulo')