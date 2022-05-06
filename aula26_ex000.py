# função para realizar a soma dos elementos de uma lista
def somarelementoslista(inteiros):
    soma=0
    for valor in inteiros:
        soma+=valor
    return soma
print(somarelementoslista([3,4,6,9,10,23,13]))