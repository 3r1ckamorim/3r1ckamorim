#5! 5X4X3X2X1=120




n=int(input('Digite um número para calcular seu fatorial: '))
c=n
f=1
print('Calculando {}! ='.format(n), end='')
while c>0:
    print('{}'.format(c),end='')
    print(' X 'if c>1 else ' = ', end='')
    f*=c #f=f*c
    c-=1 #c=c-1
print('{}'.format(f))