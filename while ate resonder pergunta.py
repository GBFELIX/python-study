n1 = str(input('digite M ou F')).strip().upper()[0]
while n1 not in 'FfMm':
    n1 = str(input('digite novamente M ou F')).strip().upper()[0]
print('O sexo escolhido foi {}'.format(n1))