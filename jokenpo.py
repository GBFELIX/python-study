import random

x = int(input('digite 1 para pedra, 2 papel e 3 tesoura'))
if x == 1:
    x = 'pedra'
elif x == 2:
    x = 'papel'
elif x == 3:
    x = 'tesoura'
y = ['pedra', 'papel', 'tesoura']
z = random.choice(y)
if x == 'pedra' and z == 'tesoura':
    print('você ganhou')
elif x == 'papel' and z == 'pedra':
    print('você ganhou')
elif x == 'tesoura' and z == 'papel':
    print('você ganhou')
elif x == 'tesoura' and z == 'pedra':
    print('você perdeu')
elif x == 'pedra' and z == 'papel':
    print('você perdeu')
elif x == 'papel' and z == 'tesoura':
    print('você perdeu')
elif x == z:
    print('Empate')
print('Computador escolheu {}'.format(z))
