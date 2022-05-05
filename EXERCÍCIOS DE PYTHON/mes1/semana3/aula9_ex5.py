no1=int(input('Digite a primeira nota do aluno: '))
no2=int(input('Digite a segunda nota do aluno: '))
media=no1+no2/2
if media<5:
    print('REPROVADO')
elif media>=5 and media<7:
    print('RECUPERAÇÃO')
elif media>=7:
    print('APROVADO')
