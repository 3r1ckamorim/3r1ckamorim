num=cont=soma=0
while num!=999:
    soma+=num
    cont+=1
    num=int(input('Digite um número ou 999 para parar: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma} .')   