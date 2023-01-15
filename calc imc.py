x = float(input('digite seu peso'))
y = float(input('digite sua altura'))
z = x / (y * y)
if z > 40:
    print('Obesidade morbida')
elif 40 > z >= 30:
    print('obesidade')
elif 30 > z > 25.5:
    print('sobre peso')
elif 25.5 > z > 18.5:
    print('peso ideal')
elif 18.5 < z:
    print('abaixo do peso')
print(x, y, z)