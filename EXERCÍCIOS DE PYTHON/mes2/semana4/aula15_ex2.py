
maior=0
menor=500
for c in range(0,5):
    peso=float(input('Digite o peso de 5 pessoas: '))
    if peso>maior:
        maior=peso
    if peso<menor:
        menor=peso
print('maior = ',maior, 'Menor = ',menor)
print('A quantidade de homens com mais de 18 é')