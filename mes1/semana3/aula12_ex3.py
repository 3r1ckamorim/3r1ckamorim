print('Me informe a estatura de 3 pessoas')
esta1=input('Estatura da primeira pessoa: ')
esta2=input('Estatura da segunda pessoa: ')
esta3=input('Estatura da terceira pessoa: ')
if esta1>esta2>esta3:
    print(esta1,esta2,esta3)
elif esta2>esta1>esta3:
    print(esta2,esta1,esta3)
elif esta1>esta3>esta2:
    print(esta1,esta3,esta2)
elif esta2>esta3>esta1:
    print(esta2,esta3,esta1)
elif esta3>esta1>esta2:
    print(esta3,esta1,esta2)
elif esta3>esta2>esta1:
    print( esta3,esta2,esta1)