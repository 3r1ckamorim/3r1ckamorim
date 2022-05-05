nu=int(input('Digite um numero:'))
nu2=int(input('digite um numero:'))
nu3=int(input('digite um numero:'))
maior=nu
if(nu2>maior):
    maior=nu2
if(nu3>maior):
    maior=nu3

print('o Maior numero é {}.'.format(maior))

maior=nu
if(nu2<maior):
    maior=nu2
if(nu3<maior):
    maior=nu3

print('o Menor numero é {}.'.format(maior))