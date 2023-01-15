import random

x = int(input('Digite um valor'))
y = str(input('digite P/I'))
tent = 0
b = str('s')
a = str('s')
while b == a:
    r = random.randrange(0, 10)
    z = (x + r) % 2
    if z == 0:
        a = "p"
        print(f'você jogou {x} e o pc {r} o total deu {x+r} deu par')
    else:
        a = 'i'
        print(f'você jogou {x} e o pc {r} o total deu {x + r} deu impar')
    if y == a:
        tent += 1
        print(f'Você ganhou')
        a = 's'
        x = int(input('vamos continuar, digite um valor'))
        y = str(input('digite P/I'))
    elif y != a:
        print(f'você perdeu, você venceu {tent} vezes')
        break









