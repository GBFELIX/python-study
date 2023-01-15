x = int(input('Digite um valor'))
y = int(input('Digite um valor'))
z = 0
while z != 5:
    print('''[-Digite 1 para somar-]    
[-Digite 2 para multiplicar-] 
[-Digite 3 para ver qual é maior-]
[-Digite 4 para adicionar novos valores-]  
[-Digite 5 para sair-] ''')
    z = int(input('>>>>>Digite uma opção<<<<<'))
    if z == 1:
        print(f'A soma dos valores é igual a {x + y}')
    if z == 2:
        print(f'A multiplicação dos valores é igual a {x * y}')
    if z == 3:
        if x > y:
            print('o maior valor é {}'.format(x))
        elif y > x:
            print('o maior valor é {}'.format(y))
        elif x == y:
            print('Os valores são iguais')
    if z == 4:
        print('Digite novamente')
        x = int(input('Digite um valor'))
        y = int(input('Digite um valor'))
    if z == 5:
        print('finalizando')
    print('=-=' * 10)
print('fim da aplicação')

