x = int(input('digite a quantia que quer sacar'))
while True:
    c = x / 50
    rest1 = x % 50
    print(f'{int(c)} notas de 50R$')
    v = rest1 / 20
    rest2 = rest1 % 20
    print(f'{int(v)} notas de 20R$')
    d = rest2 / 10
    rest3 = rest2 % 10
    print(f'{int(d)} notas de 10R$')
    u = rest3 / 1
    print(f'{int(u)} notas de 1R$')
    break
