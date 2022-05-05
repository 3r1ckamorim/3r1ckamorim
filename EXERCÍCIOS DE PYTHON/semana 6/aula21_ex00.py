'''dias=('domigo','segunda','terça','quarta','quinta','sexta','sábado')

dias=()

print(type(dias))

print(dias[3])'''

'''texto='python'
tuple(texto)
print(tuple(texto))
texto[2]='e'
print(texto)''' #nao funcionará como tupla#

'''lista=[1,2,3,4]
lista[2]=8
print(tuple(lista)) #funciona como lista#'''

'''lista=[3,5]
tupla1=(1,2,lista)
tupla2=(1,2,lista[0],lista[1])
#print(tupla)
#print(tupla[2])
#print(len(tupla1),len(tupla2))
print(tupla2.count(2))
lista=['python',1,2,'java']
print(lista)'''

'''meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
#print(len(meses))
n=1
while n<4:
    mes=int(input('Escolha um mês [1-12]: '))
    if 1<=mes<13:
        print(f'O mês é {meses[mes-1]}')
    n+=1'''

'''meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
print(meses[:-3])'''

meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro']
#meses.append('janaina')
#print(meses)

#meses+=['janaina','zé']
#print(meses)


for mes in meses:
    print(mes,end='')