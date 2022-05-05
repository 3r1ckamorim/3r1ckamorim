from random import randrange
m=1
n=int(input('Informe o valor para N que seja maior que 1: '))

if n>1:
    l=[randrange(1,11) for i in range(n)]
    for i in l:
        m*=i

    l2=m**1/n
    print('Alista criada foi: ',l)
    print('A média geométrica da lista será: ',l2)
else:
    print('ERROR \nO valor N deve ser maior que 1!')