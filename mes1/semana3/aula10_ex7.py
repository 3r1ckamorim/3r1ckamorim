car=int(input('Qual o seu cargo: \n Programador de Sistemas=1  Analista de Sistemas=2  Analista de Banco de Dados=3 '))
sal=int(input('Qual o seu salário'))
if car==1:
    au=sal*1.30
    print('O salário após o aumento ficará {}.'.format(au))
elif car==2:
    au=sal*1.20
    print('O salário após o aumento ficará {}.'.format(au))
elif car==3:
    au=sal*1.15
    print('O salário após o aumento ficará {}.'.format(au))
elif car<1 and car>3:
    print('inválido')