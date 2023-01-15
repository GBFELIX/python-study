from random import randint
x = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(x)
y = min(x)
z = max(x)

print(f'O menor valor é ' + str(y))
print(f'O maior valor é ' + str(z))