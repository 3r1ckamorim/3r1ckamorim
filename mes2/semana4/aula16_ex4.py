nome=str(input('Digite o nome dos nadadores: '))
tempo=int(input('Digite o tempo desse nadador: '))
nome1=nome
nome2=nome
pior=tempo
melhor=tempo
soma=0
soma+=tempo
tempo12s15s=0
if 12<= tempo<=15:
    tempo12s15s+=1
for c in range(0,6):
    nome=str(input('Digite o nome do nadador: '))
    tempo=float(input('Digite o tempo desse nadador: '))
    if tempo>melhor:
        tempo=melhor
        nome1=nome
    elif tempo<pior:
        tempo=pior
        nome2=nome
    if 12<= tempo<=15:
        tempo12s15s+=1
print('O melhor tempo foi {}s do nadador {}.'.format(melhor,nome1))
print('O pior tempo foi {}s do nadador {}.'.format(pior,nome2))
media=soma/7
print('A média de todos os tempos é', media)

print('Atletas entre 12s e 15s', tempo12s15s)