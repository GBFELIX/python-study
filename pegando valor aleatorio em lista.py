import random

a = str(input("digite um nome"))
b = str(input("digite outro nome"))
c = str(input("digite outro nome"))
d = str(input("digite outro nome"))

lista = [a, b, c, d]
esc = random.choice(lista)
print('quem foi escolhido para o qt foi o {}'.format(esc))