n = 0
ve = 0
no = 0
while n < 5:
    n += 1
    p = int(input('digite a idade da {}ª pessoa'.format(n)))
    x = p - 18
    if x < 0:
        no += 1
    else:
        ve += 1
print('tem {} menores de idade e {} maiores de idade'.format(no, ve))
