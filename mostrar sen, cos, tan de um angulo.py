import math

ang = float(input("digite o angulo"))
seno = math.sin(math.radians(ang))
print("o angulo de {:.2f} tem seno de {:.2f}".format(ang, seno))
cos = math.cos(math.radians(ang))
print("o angulo de {:.2f} tem coseno de {:.2f}".format(ang, cos))
tan = math.tan(math.radians(ang))
print("o angulo de {:.2f} tem tangente de {:.2f}".format(ang, tan))