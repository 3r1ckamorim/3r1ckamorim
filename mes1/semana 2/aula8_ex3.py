qkm=float(input('Qual a quantidade de quilometros percorridos pelo carro alugado: '))
qdia=float(input('Qual a quantidade de dias pelos quais o carro foi alugado: '))
pdia=qdia*60
pkm=qkm*0.15
apagar=pdia+pkm
print('O preço a pagar fica {}.'.format(apagar))