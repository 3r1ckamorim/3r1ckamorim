quantidade=float(input('quantos qual a distincia viajada em km?'))
if quantidade<=200:
    preco=quantidade*0.50
    print('o valor da passagem é de {}.'.format(preco))
else:
    preco=quantidade*0.45
    print('o valor da passagem é de {}.'.format(preco))

