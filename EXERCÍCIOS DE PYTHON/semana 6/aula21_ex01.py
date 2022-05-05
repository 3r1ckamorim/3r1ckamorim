lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
maiorvalor=lista[0]
menorvalor=lista[0]
listapares=[]
ocorrencia=0
mediaelementos=0
somanegativa=0
for index in range(0,len(lista)):
    #maior valor
    if maiorvalor<lista[index]:
        maiorvalor=lista[index]
    #menor valor
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    #lista números páres
    if lista[index]%2==0:
        listapares.append(lista[index]) #Listapares=[12]
    #Ocorrência primeiro elemento
    if lista[index]==lista[0]:
        ocorrencia+=1
    #somatoria para média
    mediaelementos+=lista[index]
    # soma numeros negativos
    if lista[index]<0:
        somanegativa+=lista[index]
#media
mediaelementos/=len(lista)
print(f'Maior valor: {maiorvalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listapares}')
print(f'Número de ocorrências do primeiro elemento: {ocorrencia}')
print(f'Media de elementos: {mediaelementos}')
print(f'Soma dos números negativos: {somanegativa}')