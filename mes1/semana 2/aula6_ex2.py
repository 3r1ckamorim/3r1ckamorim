velocarro=float(input('qual a velocidade do carro:'))
acima= velocarro-80
multa=acima*7
if velocarro>80:
    print('o motorista foi multado, terá que pagar {} de multa.'.format(multa))
else:
    print('o motorista não foi multado')