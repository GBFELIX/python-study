
x = int(input('digite um numero pra ver qual é maior'))
y = int(input('digite um numero '))
z = int(input('digite um numero '))
if x > y and x > z:
    print('o maior numero é {}'.format(x))
if y > x and y > z:
    print('o maior numero é {}'.format(y))
if z > y and z > x:
    print('o maior numero é {}'.format(z))
if x < y and x < z:
    print('o menor numero é {}'.format(x))
if y < x and y < z:
    print('o menor numero é {}'.format(y))
if z < y and z < x:
    print('o menor numero é {}'.format(z))