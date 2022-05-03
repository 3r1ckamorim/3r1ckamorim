preco=int(input('Qual o valor do produto: '))
paga=int(input('escolha a forma de pagamento: \n 1) à vista dinheiro/cheque 10 porcento de desconto. \n 2) à vista no cartão: 5 porcento de desconto \n 3) em até 2x no cartão: preso normal. '))
if paga==1:
    valor=preco*0.9
    print('O valor a ser pago será {}.'.format(valor))
elif paga==2:
    valor=preco*0.95
    print('O valor a ser pago será {}.'.format(valor))
elif paga==3:
    valor=preco
    print('O valor a ser pago será {}.'.format(valor))
elif paga<1 and paga>4:
   print('invalido')