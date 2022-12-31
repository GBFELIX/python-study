cont = maior = menor = m = contador = 0
stop = str()
while stop != 'n':
    x = int(input('Digite outro valor para ser somado'))
    contador += x
    cont += 1
    stop = str(input('Você deseja continuar? (S/N): '))
    if cont == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
m = contador / cont
print('Você digitou {} valores e a soma dos valores é igual a {}, a media é igual a {}'.format(cont, contador, m))
print('O maior valor digitado foi {} e menor foi {}'.format(maior, menor))
