import random

n = int(input('digite um numero ate 5'))
x = random.randrange(0, 5)
if n == x:
    print('acerto')
    print('computador escolheu ', x)
else:
    print('errou')
    print('computador escolheu ', x)
