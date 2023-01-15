i = int(input('digite a idade'))
s = str(input('digite o sexo [H/M]'))
ft = a = m = h = 0

while ft == 0:
    while s not in "HhMm":
        s = str(input('digite o sexo [H/M]'))
    if i >= 18:
        a += 1
    if s in "Hh":
        h += 1
    if s in "Mm" and i == 19 or i == 18 or i < 18:
        m += 1
    b = str(input('deseja continuar? [S/N]'))
    while b not in "SsNn":
        b = str(input('deseja continuar? [S/N]'))
    if b != "s":
        ft += 1
        print(f' {a} pessoas com mais de 18 anos // {h} homens cadastrados // {m} mulheres com menos de 20 anos')
        print('Programa finalizado')
        break
    i = int(input('digite a idade'))
    s = str(input('digite o sexo [H/M]'))