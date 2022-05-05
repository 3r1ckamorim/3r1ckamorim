from random import randrange #cria uma lista de números aleatórios

linha=int(input('Números de linhas: '))
coluna=int(input('Números de colunas: '))

a=[[randrange(1,11)for i in range(coluna)] for j in range(linha)] #criando matriz aleatória
b=[[randrange(1,11)for i in range(coluna)] for j in range(linha)] #criando matriz aleatória

abaixodp=0
acimadp=0

for i in range(linha):
    for j in range(coluna):
        if i>j:
            abaixodp+=a[i][j]
        if i<j:
            acimadp+=b[i][j]

print('Matriz A: ')
for i in range(linha):
    for j in range(coluna):
        print(a[i][j], end=' ')
    print()

print('Matriz B: ')
for i in range(linha):
    for j in range(coluna):
        print(b[i][j], end=' ')
    print()

print(f'Soma= {abaixodp+acimadp}')