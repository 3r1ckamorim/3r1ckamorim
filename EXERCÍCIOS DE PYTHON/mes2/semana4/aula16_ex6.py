print('Código de cargo: \n1 : Enfermeiro \n2 : Nutricionista \n3 : Médico(a)')
qtdenutri=0
total_sal_nutri=0
while True:
    cargo=int(input('informe um código de cargo: '))
    if cargo>=1 and cargo<=3:
        salario=float(input('Salário R$: '))
        if cargo ==2:
            qtdenutri+=1
            total_sal_nutri+=salario
        resp=input('Deseja continuar [S/N]: ')
        if resp.upper()=='N':
            break
    else:
        print('Código Inválido!')
if qtdenutri>0:
    media=total_sal_nutri/qtdenutri
    print(f'Média salário das nutricinistas R$: {media:.2f}')
else:
    print('Não foram inseridos dados sobre as nutricionistas.')