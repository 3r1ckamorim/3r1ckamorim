va=int(input('Qual o valor da camisa comprada: '))
nu=int(input('Quantas o comprador levará: '))
preco=va*nu
if nu<=5:
    disc=preco*0.97
    print('O valor a se pagar será de {}.'.format(disc))
elif nu>5 and nu<=10:
    disc=preco*0.95
    print('O valor a se pagar será de {}.'.format(disc))
elif nu>10:
    disc=preco*0.93
    print('O valor a se pagar será de {}.'.format(disc))