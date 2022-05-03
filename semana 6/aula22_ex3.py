from random import choice, shuffle
lista=[]
while True:
    li=str(input('Digite o nome das pessoas que compraram a rifa (quando quiser parar digite 0): '))
    lista.append(li)
    resp=input('Deseja continuar S/N: ')
    if resp.upper()=='N':
        break
shuffle(lista)
ale=choice(lista)
print(f'A pessoa sorteada foi {ale}')