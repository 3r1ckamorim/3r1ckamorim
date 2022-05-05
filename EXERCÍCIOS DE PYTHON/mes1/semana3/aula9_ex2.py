nu=int(input('Digite um número:'))
carai=int(input('Escolha a base de conversão 1= Binário, 2= Octal pu 3= Hexadecimal.'))
if carai==1:
    print('O binário desse número será {}.'.format(bin(nu)))
elif carai==2:
    print('O octal desse número será {}.'.format(oct(nu)))
elif carai==3:
    print('O hexadecimal desse número será {}.'.format(hex(nu)))