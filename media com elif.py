x = float(input('digite a primeira nota do aluno'))
y = float(input('digite a segunda nota do aluno'))
z = (x + y) / 2
if z >= 7:
    print('aprovado')
elif 5 <= z < 6.9:
    print('recuperação')
elif z < 5:
    print('reprovado')