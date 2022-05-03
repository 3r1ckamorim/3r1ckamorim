salario=int(input('digite o salário do funcionário:'))
if salario>1250:
    aumento=salario*1.10
    print('o novo salário do funcionário será {}.'.format(aumento))
else:
    aumento=salario*1.15
    print('O novo salário do funcionário é de {}.'.format(aumento))