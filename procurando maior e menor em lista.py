x = list()
for i in range(5):
    a = int(input('digite um numero'))
    x.append(a)
print(x)
print(f'o maior numero é {max(x)} e sua Posição é {x.index(max(x))}')
print(f'o menor numero é {min(x)} e sua Posição é {x.index(min(x))}')