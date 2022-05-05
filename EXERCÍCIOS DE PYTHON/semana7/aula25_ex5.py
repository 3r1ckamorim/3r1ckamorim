from random import randrange

linha=int(input('Números de linhas: '))
coluna=int(input('Números de colunas: '))

a=[[randrange(0,2)for i in range(coluna)] for j in range(linha)]
b=[[randrange(0,2)for i in range(coluna)] for j in range(linha)]
print('Matriz A: ')
for i in range(linha):
    for j in range(coluna):
        print(a[i][j], end=' ')
    print()
soma=a[i][j]
if soma==0:
    print('É Matriz Nula.')
else:
    print('Não é matriz nula.')