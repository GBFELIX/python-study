import math

ca = float(input("digite o cateto adjascente"))
co = float(input('digite o cateto oposto do triangulo retangulo'))
hi = math.hypot(ca, co)
print("a hipotenusa do triangulo retangulo vai medir {:.2f}".format(hi))