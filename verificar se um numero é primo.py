n = int(input('digite um numero inteiro: '))
divisor = 0
for c in range(1, n+1):
    if n % c == 0:
        divisor += 1
if divisor == 2:
    print(f'O numero é primo com apenas {divisor} números divisíveis por {n}.')
else:
    print(f'O numero Não é primo, pois tem {divisor} números divisíveis por {n}.')

