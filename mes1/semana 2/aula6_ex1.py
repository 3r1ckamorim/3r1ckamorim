from random import randint
re=int(input('adivinhe um numero entre 0 e 5:'))
n=randint(1,5)
if n!=re:
    print('Perdeu')
else:
    print('Venceu')
