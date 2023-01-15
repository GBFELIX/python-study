x = int(input('digite um valor'))
y = int(input('digite 1 para transformar em binario, 2 para octal e 3 para hexadecimal'))
if y == 1:
    a = bin(x)
    print('o numero {} em binario fica {}'.format(x, a))
elif y == 2:
    b = oct(x)
    print('o numero {} em octal fica {}'.format(x, b))
elif y == 3:
    c = hex(x)
    print('o numero {} em hexadecimal fica {}'.format(x, c))