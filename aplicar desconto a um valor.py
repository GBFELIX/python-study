val = int(input('digite a valor'))
por = int(input('digite a procentagem do desconto'))
disc = val / 100 * por
vt = val - disc
print("valor total {} e desconto de {} valor final de {}".format(val, disc, vt))
