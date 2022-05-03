cidade=str(input("Digite o nome de uma cidade e lhe direi se começa com Santa: "))
pri= cidade.split()
pri2=pri[0]
ki='Santa'
if pri2==ki:
    print('A cidade {} começa com Santa.'.format(cidade))
else:
    print('A cidade {} não começa com Santa.'.format(cidade))