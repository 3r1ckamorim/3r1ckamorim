vcasa=float(input('Qual o valor da casa:'))
scomp=float(input('Qual o salário do comprado:'))
ano=float(input('Em quantos anos ele vai pagar:'))
mes=12*ano
prest=scomp/mes
porcento=scomp*0.30
if prest<scomp:
    print('O empréstimo foi aprovado')
else:
    print('O empréstimo foi negado')
