maior=0
menor=0
for data in range(7):
    data=int(input('Informe a data de nascimento de 7 pessoas: '))
    ani=2022-data
    if ani>=18:
        maior+=1
    else:
        menor+=1
print('são menores de idade {} e são maiores de idade {}.'.format(menor, maior))