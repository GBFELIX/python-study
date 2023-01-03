n = str(input('digite o nome do produto'))
p = float(input('digite o preço do produto'))
pb = ''
vt = pc = pbp = cont = 0
while True:
    vt += p
    cont += 1
    if p >= 1000:
        pc += 1
    if cont == 1:
        pbp = p
        pb = n
    else:
        if p < pbp:
            pb = n
    n = str(input('digite o nome do produto, digite "fim" para fechar o carrinho'))
    if n in 'fim':
        print('acabaram as compras')
        print(f' {vt}R$ foi o valor total das compras. {pc} produtos custam mais de mil reais. E {pb} é o produto mais barato do carrinho')
        break
    p = int(input('digite o preço do produto'))

