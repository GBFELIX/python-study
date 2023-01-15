x = (int(input('digite um numero: ')),
    int(input('digite outro numero: ')),
    int(input('digite nais um numero: ')),
    int(input('digite um ultimo numero: ')))

print(f'você digitou os seguintes numeros {x}')
print(f'O numero 9 apareceu {x.count(9)} vezes')
print(f'O numero 3 aparceu na {x.index(3) + 1}ª posição')
print(f'Os valores que sao pares sao ', end='')
for a in x:
    if a % 2 == 0:
        print(a, end=" ")
