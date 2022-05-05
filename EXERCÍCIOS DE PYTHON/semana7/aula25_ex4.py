from random import randrange

jogos=int(input('Informe quantos jogos serão gerados: '))
n=6
c=0
while c<jogos:
    if n>0:
        números=[randrange(1,61) for i in range(n)]
        c+=1
        print(números)
