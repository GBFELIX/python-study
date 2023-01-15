x = int(input('Digite um valor'))
a = str('s')
cont = 1

while a in 'Ss':
    while cont < 11:
        if x < 0:
            print('numero invalido')
            break
        y = x * cont
        print(f'{x} x {cont} = {y}')
        cont += 1
    z = str(input('deseja continuar? [S/N]'))
    a = z
    if a == 'n':
        print('programa encerrado')
        break
    x = int(input('Digite um valor'))
    cont = 1




