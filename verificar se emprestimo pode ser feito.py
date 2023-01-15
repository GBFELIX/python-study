x = int(input('digite o valor da casa'))
y = int(input('digite o seu salario'))
z = int(input('digite o tempo em anos'))
trint = (y / 10) * 3
meses = z * 12
valmen = x / meses

if valmen <= trint:
    print('emprestimo aprovado no valor de {}R$ como duração de {} meses, valor mensal de {:.8}'.format(x, meses, valmen))
else:
    print('emprestimo negado')
