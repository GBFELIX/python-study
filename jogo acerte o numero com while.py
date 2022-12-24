import random
tent = 0
n = int(input('digite um numero ate 5'))
x = random.randrange(0, 5)

if n == x:
    tent += 1
    print('acerto, computador escolheu {} e você precisou de {} tentativa'.format(x, tent))
else:
    while x != n:
        tent += 1
        n = int(input('errou, computador escolheu {}, digite outro numerode de 0 ate 5'.format(x)))
        x = random.randrange(0, 5)
        if n == x:
            tent += 1
            print('')
            print('acerto, computador escolheu , {} você precisou de {} tentativas para acertar'.format(x, tent))



