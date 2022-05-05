
sexo=''
while sexo!='F' or sexo!='M':
    sexo=str(input('Qual o seu sexo M ou F: ')).strip().upper()
    if sexo=='M':
        print('seu sexo é masculino')
        break
    if sexo=='F':
        print('seu sexo é feminino')
        break