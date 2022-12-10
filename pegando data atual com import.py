from datetime import date
ve = 0
no = 0
ano = date.today().year
for n in range(1, 7):
    p = int(input('digite o ano que a {}ª pessoa nasceu'.format(n)))
    x = ano - p
    if x < 18:
        no += 1
    else:
        ve += 1
print('tem {} menores de idade e {} maiores de idade'.format(no, ve))
