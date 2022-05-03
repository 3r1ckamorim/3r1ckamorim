homem=0
mulher=0
parar=False
print('Vamos fazer uma pequena entrevista: ')
while not parar:
    sexo=str(input('Me diga o sexo [F/M] do aluno: ')).strip().upper()
    idade=int(input('Me diga a idade do aluno: '))
    if idade>=18 and sexo=='M':
        homem+=1
    if sexo=='F':
        mulher+=1
    if idade<0:
        print('Encerrando entrevista')
        parar=True
print('A quantidade de homens com mais de 18 é', homem)
print('A quantidade de mulheres de qualquer idade é', mulher)

