print('## programa de emprestimos ## \n responda: 0 - não e 1 - sim')
nomeNegativado=int(input('possui nome negativado?'))
if nomeNegativado==1:
    print('Não pode realizar emprestimo')
else:
    carteiraAssinada=int(input('possui carteira assinada?'))
    if carteiraAssinada==0:
        print('Não pode realizar o emprestimo')
    else:
        possuiCasaPropria=int(input('possui casa própria?'))
        if possuiCasaPropria==0:
             print('Não pode realizar empréstimo')
        else:
             print('Concede o empréstimo')
