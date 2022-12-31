x = int(input('Digite um valor'))
a = str('s')
cont = 1
while cont < 11:
    y = x * cont
    print(f'{x} x {cont} = {y}')
    cont += 1
    if a == 'Ss':
        z = str(input('deseja continuar?'))
        x = int(input('Digite um valor'))
        a = z
        cont = 1
