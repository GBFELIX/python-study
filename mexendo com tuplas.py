print('colocados da seleção de um ano')
n = 'Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético', 'Mineiro'
print('''[-Digite A para mostrar os 5 primeiros colocados-]    
[-Digite B para mostrar os 4 ultimos colocados-] 
[-Digite C para ver lista em ordem alfabetica-]
[-Digite D em que posição da tabela esta o  flamengo -]''')
x = str(input('Digite uma opção'))
if x == 'a':
    print('Os 5 primeiros colocados da tabela são ', end='')
    print(n[:4])
if x == 'b':
    print('Os 4 ultimos colocados da tabela são ', end='')
    print(n[7:])
if x == 'c':
    print(sorted(n))
if x == 'd':
    print('A posição do flamengo na tabela é ', end='')
    print(n.index('Flamengo'))