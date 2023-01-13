x = list()
for i in range(5):
    a = int(input('digite um numero'))
    x.append(a)
print(x)
print(f'o maior numero é {max(x)}')
print(f'o menor numero é {min(x)}')
print(f'Posição do maior {x.index(max(x))}')
print(f'Posição do menor {x.index(min(x))}')