x = float(input('digite o ano de nascimento do atleta'))
y = 2022 - x

if y <= 9:
    print('mirim')
elif 10 <= y <= 14:
    print('infantil')
elif 15 <= y <= 19:
    print('junior')
elif y == 20:
    print('senior')
elif y > 20:
    print('master')