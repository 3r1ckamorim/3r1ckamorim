soma=0
maior=0
mulhermen=0
novelho=0
media=0
print('Você irá informar o nome, idade e sexo de 4 pessoas')
for c in range(4):
    nome=str(input('Digite o nome da pessoa: ')).strip()
    idade=int(input('Digite a idade da mesma pessoa : '))
    sexo=str(input('Digite o sexo [F/M] das mesmas 4 pessoas na mesma ordem: ')).strip().upper()
    soma+=idade
    if c==1 and sexo in 'M':
        maior=idade
        novelho=nome
    if sexo in 'M' and idade>maior:
        maior=idade
        novelho=nome
    if sexo in 'F' and idade<20:
        mulhermen+=1
media=soma/4
print('A media de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idade,nome))
print('A quantidade de mulheres com menos de 20 é {}.'.format(mulhermen))

#num ta pronto


