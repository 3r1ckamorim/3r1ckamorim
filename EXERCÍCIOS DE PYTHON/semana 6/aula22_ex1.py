'''nu1=int(input('Me informe um número: '))
nu2=int(input('Me informe um número: '))
nu3=int(input('Me informe um número: '))
nu4=int(input('Me informe um número: '))

# ^ Tambem podia por tudo numa linha só
lista=nu1,nu2,nu3,nu4
tuplapares=[]
pares=0
nove=lista.count(9)
print(f'A quantidade de noves que você digitou foi: {nove}')

tres=(lista.index(3)+1)
print(f'O primeiro numero três esta na casa: {tres}')

for index in range(0,len(lista)):
    if lista[index]%2==0:
        tuplapares.append(lista[index])
print(f'Os pares são: {tuplapares}')'''

# agora usando lista

num=[]
for n in range(0,4):
    num.append(int(input('digite um número: ')))
tuplapares=[]
pares=0
nove=num.count(9)
print(f'A quantidade de noves que você digitou foi: {nove}')

tres=(num.index(3)+1)
print(f'O primeiro numero três esta na casa: {tres}')

for index in range(0,len(num)):
    if num[index]%2==0:
        tuplapares.append(num[index])
print(f'Os pares são: {tuplapares}')


