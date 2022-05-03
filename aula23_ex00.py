# Converter tupla em lista

'''dias=('Domingo','segunda','terca','quarta','quinta','sexta','sabado')
semana=list(dias)
print(f'A variável semana é do tipo {type(semana)} e contêm os dias da {semana}.')'''

num=[]
for n in range(0,10):
    num.append(n**2)
print(num)

# LISTAS COMPRIMIDAS
lista1=[x**2 for x in range(10)] #versao simplificada da anterior que da no mesmo resultado
print(lista1)

lista2=[x for x in range(1,20) if x%2==0] # vai mostrar só os pares entre 1 a 20
print(lista2)

lista3=[i for i in "HACATHON" if i in ['A' , 'E', 'I', 'O', 'U']] # inserindo as vogais de uma string em uma lista
print(lista3)

lista4=[1,2,3]
lista4=[i**3 for i in lista4] # atribuir novos valores aos elementos da lista através de uma operação
print(lista4)