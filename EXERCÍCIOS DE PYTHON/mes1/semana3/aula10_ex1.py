ano=int(input('Qual o ano de nascimento do atleta: '))
idade=2022-ano
if idade<=9:
    print('Categoria Mirim')
elif idade<=14:
    print('Categoria Infantil')
elif idade<=19:
     print('Categoria Junior')
elif idade<=25:
     print('Categoria Sênior')
elif idade>25:
    print('Categoria Matter')