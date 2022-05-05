pares=0
for cont in range(5):
    num=int(input('Digite um numero: '))
    if num%2==0:
        pares+=1
print('Quantidade de números pares digitados: {}.'.format(pares))