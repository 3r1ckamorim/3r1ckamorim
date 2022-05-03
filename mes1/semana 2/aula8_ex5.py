from random import shuffle
alu1=str(input('Digite o nome do primeiro aluno: '))
alu2=str(input('Digite o nome do segundo aluno: '))
alu3=str(input('Digite o nome do terceiro aluno: '))
alu4=str(input('Digite o nome do quarto aluno: '))
lista=[alu1,alu2,alu3,alu4]
shuffle(lista)
print('A ordem será {} primeiro, {} segundo, {} terceiro e {} quarto.'.format(lista[0],lista[1],lista[2],lista[3]))