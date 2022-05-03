nu=int(input('Digite um numero positivo:'))
nu2=int(input('Digite mais um numero positivo:'))
menu=int(input('menu: \n 1. Média ponderada, com pesos 2 e 3, respectivamente \n 2. Quadrado da soma dos 2 números \n 3. Cubo do menor número \n Escolha uma opção:'))
media_pon=nu*2+nu*3/5
quadrado=(nu+nu2)**2
menor=nu

if(nu2<menor):
    maior=nu2
    cubo=menor**3
else:
    if menu==1:
        print('media ponderada igual a {:.2f}.'.format(media_pon))
    else:
        if menu==2:
         print('O quadrado da soma dos 2 numeros é {:.2f}.'.format(quadrado))
        else:
            if menu==3:
                cubo=menor**3
                print('O cubo da soma é {}.'.format(cubo))
            else:
                print('opção inválida')

                # pode usar elif ao invés de if seguido de else #


