def exibirmensagem(): # Declarando uma função
    print('Python é facil')
exibirmensagem() # Chamando a execução da função

def exibirmensagemboasvindas(pessoa, mensagem): # Função com passagem de paramêtro
    print(f'{mensagem}, {pessoa}')
exibirmensagemboasvindas('Janaina','bem-Vinda')

def exibirmensagemboasvindas(pessoa='Fulano', mensagem='Bem-vindo'):
    print(f'{mensagem}, {pessoa}')
exibirmensagemboasvindas()