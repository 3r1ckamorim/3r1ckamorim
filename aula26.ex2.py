'''def escreva(texto):
    return texto

texto=input('Escreva uma frase: ')
print(escreva(texto))'''

def escreva(msg):
    tam=len(msg)+4
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)

#programa principal
#Mensagem fixa no código
escreva('Na aula de hoje estudamos funções em python')
escreva('Turma inf 9 - SENAC - SCS')
# Mensagem digitada do usuário
escreva(input('Digite uma frase: '))