c1 = 0
c2 = 0
for c in range(0, 6):
    n = int(input('digite o ano de nascimento: '))
    x = 2022 - n
    if x > 18:
        c1 += 1
    else:
        c2 += 1
print('{} ja atingiram a maioridade e {} nao atingiram a maioridade'.format(c1, c2))