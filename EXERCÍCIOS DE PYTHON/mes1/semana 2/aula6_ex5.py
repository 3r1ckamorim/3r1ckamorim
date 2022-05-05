numeroint=float(input('digite um numero inteiro positivo:'))
re=numeroint%2
if re==0:
    nu=numeroint**2
    print('o numero é par e elevado ao quadrado fica {}.'.format(nu))
else:
    nu=numeroint**3
    print('O numero é impar e elevado ao cubo fica {}.'.format(nu))