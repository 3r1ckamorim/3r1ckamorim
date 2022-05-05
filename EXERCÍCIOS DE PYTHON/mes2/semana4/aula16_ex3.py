erros=0
for c in range(3,0,-1):
    senha=int(input('Informe a sua senha: '))
    if senha==123456:
        print('Olá! Seja bem-vindo ao nosso banco!')
        break
    elif senha!=123456:
            print('Senha incorreta! Você ainda tem {} tentativas'.format(c))
            erros+=1
    elif senha!=123456 and erros==3:
        print('“Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')