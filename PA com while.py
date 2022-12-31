v = int(input('Digite o termo inicial da P.A: '))
r = int(input('Digite a razão deste P.A: '))
vcomp = 0
vcomp1 = 10
stop = str()
while stop != 'n':
    while vcomp != vcomp1:
        print('{} -> '.format(v), end='')
        v += r
        vcomp += 1
    stop = str(input('Você deseja continuar com a P.A? (S/N): '))
    if stop == 'n':
        stop = 'n'
        print('A P.A mostrou {} valores'.format(10 + vcomp))
    else:
        vcomp1 = int(input('Quantos termos você quer ver a mais? '))
        if vcomp1 == 0:
            print('P.A finalizada')
        vcomp = 0


#a = int(input('Primeiro termo da PA: ').strip())
#b = int(input('Razão da PA: ').strip())
#c = a
#print('{}, '.format(a), end='')
#while a != c + 9 * b:
#    a += b
#    print('{}, '.format(a), end='')
#print('fim da PA')

