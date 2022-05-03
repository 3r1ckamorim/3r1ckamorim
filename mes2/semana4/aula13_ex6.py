
pri=int(input('Digite o primeiro termo: '))
ra=int(input('digite a razão: '))
decimo=pri+9*ra
for c in range(pri,ra+decimo,ra):
    print('{}'.format(c),end='->')
print('acabou')
