menu=int(input('\n*************************************** \n CÁLCULO DE GRANDEZAS ELÉTRICAS \n *************************************** \n 1. Tensão (em Volt) \n 2. Resistência (em 0hm) \n Corrente (em Ampéres) \n *************************************** \n 1) Tensão 2) Resistência 3) Corrente:'))
if menu<1 or menu>3:
    print('Opção inválida')
elif menu==1:
    vamo1=int(input('Digite o valor de resistencia:'))
    vamo2=int(input('Digite o valor de corrente: '))
    U=vamo1*vamo2
    print('O valor de Tensão será {}Volt.'.format(U))
elif menu==2:
    vamo1=int(input('Digite o valor de tensão:'))
    vamo2=int(input('Digite o valor de corrente:'))
    R=vamo1/vamo2
    print('O valor da Resistência será de {}hm.'.format(R))
elif menu==3:
    vamo1=int(input('Digite o valor de tensão:'))
    vamo2=int(input('Digite o valor de resistência:'))
    i=vamo1/vamo2
    print('O valor de Corrente será {}Ampére.'.format(i))
    
