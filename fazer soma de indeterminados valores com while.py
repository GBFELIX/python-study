x = int(input('Digite um valor para ser somado, digite 999 para parar'))
contador = 0
cont = 0
while x != 999:
    contador += x
    cont += 1
    x = int(input('Digite um valor para ser somado, digite 999 para parar'))
print('Você digitou {} valores e a soma dos valores é igual a {}'.format(cont, contador))