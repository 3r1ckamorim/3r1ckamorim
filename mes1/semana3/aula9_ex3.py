nu1=int(input('Digite um numero: '))
nu2=int(input('Digite mais um numero: '))
maior=nu1
menor=nu1
if nu2>maior:
    maior=nu2
    print(maior, 'É o maior numero.')
if nu2<menor:
    menor=nu2
    print(menor, 'É o menor numero.')
if nu1==nu2:
    print('Não existe número maior.')