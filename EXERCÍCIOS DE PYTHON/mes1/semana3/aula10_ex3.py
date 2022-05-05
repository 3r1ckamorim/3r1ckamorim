peso=float(input('Qual o seu peso: '))
alt=float(input('Qual a sua altura: '))
imc=peso/(alt*2)
if imc<=18.5:
    print('abaixo do peso')
elif imc>=18.5 and imc<=25:
    print('peso ideal')
elif imc>=25 and imc<=30:
    print('sobrepeso')
elif imc>=30 and imc<=40:
    print('Obesidade')
elif imc>40:
    print('Obesidade mórbida')
