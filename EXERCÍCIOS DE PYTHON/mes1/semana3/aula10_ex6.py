from random import choice
bora=int(input('Vamos jogar pedra-papel-tesoura\n 1=papel, 2=tessoura, 3=pedra'))
lista=(1,2,3)
bora2=choice(lista)
if bora==bora2:
    print('Empatamos, coloquei o mesmo que você')
elif bora==1 and bora2==2:
    print('Você perdeu, eu coloquei tessoura')
elif bora==1 and bora2==3:
    print('Você venceu, eu coloquei pedra')
elif bora==2 and bora2==1:
    print('Você venceu, eu coloquei papel')
elif bora==2 and bora2==3:
    print('Você perdeu, eu coloquei pedra')
elif bora==3 and bora2==2:
    print('Você venceu, eu coloquei tessoura')
elif bora==3 and bora2==1:
    print('Você perdeu, eu coloquei papel')