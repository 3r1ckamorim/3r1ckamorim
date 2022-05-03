ano=int(input('Digite sua data de nascimento:'))
certo=2022-ano
falta=18-certo
passou=certo-18
if certo<18:
    print('ainda vai se alistar, faltam {} anos.'.format(falta))
else:
    if certo>18:
        print('Já passou a hora de se alistar, passou {} anos da hora.'.format(passou))
    else:
        if certo==18:
            print('Está na hora de se alistar')