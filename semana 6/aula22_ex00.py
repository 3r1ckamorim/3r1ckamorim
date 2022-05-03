lista=['Janaina','José','Maria','Carlos']
#for n in range(0, len(lista)):
    #print(lista[n], end=' ')
#print(lista)
#print(lista)

#lista.sort() ordenar em crescente
#print(lista)

# lista.sort(reverse=True) ordenar em decrescente
#print(lista)

#del lista[3] remove o item na casa 3
#print(lista)

#lista.remove('Janaina') remove o item indicado
#print(lista)

#lista.pop() # se nao especificado vai tirar o ultimo
#print(lista)

#lista.clear() # limpa a lista
#print(lista)

#listaa=(lista) # assim as duas vao compartilhar as alteracoes
#listaa=lista[:] # asssim nao vai alterar a outra só a alterada

listaa=('Jailson','Mendes')
#lista.extend(listaa) #junta as duas listas
#print(lista)

#print(lista.count('José')) # conta a quantidade de itens expecificados

#print(lista.index('Janaina')) #posicao do item expecificado

# para achar (MAIOR) é max (MENOR) é min

for indice, nome in enumerate(lista):
    print(f'{nome} está armazenado no índice {indice}')


#\\\\\\\\\\\\\\\\ MATRIZES \\\\\\\\\\\\\\\\\\\\ MATRIZES \\\\\\\\\\\\\\\\\\

#a=[[2,1,-5],[3,7,0],[6,4,8]]
'''print(a[0][0])
print(a[0][1])
print(a[2][0])
print(a[0][0]+a[0][1]+a[0][2])
print(a[0][0],a[0][1],a[0][2])'''

'''soma_a=0
lin=len(a)
col=len(a[0])

for i in range(lin):
    for j in range(col):
        soma_a+=a[i][j]
print(soma_a)'''