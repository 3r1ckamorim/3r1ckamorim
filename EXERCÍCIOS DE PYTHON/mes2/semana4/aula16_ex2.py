nome=(input('Digite o nome do medicamento: '))
preco=float(input('Digite o preço do medicamento: '))
soma=0
menor=preco
barato=nome
soma+=preco
for c in range(4):
    nome=(input('Digite o nome do medicamento: '))
    preco=float(input('Digite o preço do medicamento: '))
    soma+=preco
    media=soma/6
    if preco<menor:
        menor=preco
        barato=nome
print('O menor preço será {}, o nome é {} e a média aritimética dos preços informados é {}.'.format(menor,barato,media))
    