n=int(input('Digíte um número impar, ,maior que um: '))
if n<=1 or n%2==0:
    print('Número informado não atende critérios definidos!')
else:
    l=[]
    for x in range(n):
        num=int(input('Digite um número maior ou igual a zero: '))
        l.append(num)
centro=int(len(l)/2)
elementocentro=l[centro]
fatorial=1
#fatorial é tipo=1*2*3*4*5
for n in range(2, elementocentro+1):
    fatorial*=n
print(f'Lista: {l}')
print(f'O elemento do centro da lista: {elementocentro} \nE seu fatorial é igual a: {fatorial}')