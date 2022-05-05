from tkinter import _ExceptionReportingCallback
from winreg import EnableReflectionKey


sal_base=float(1500)
comissao=float(200)
no=input('Qual o nome do corretor:')
quanti=int(input('Qual a quantidade de imóveis vendidos:'))
valort=float(input('Qual o valor total de suas vendas:'))
salario=(sal_base)+(comissao*quanti)+(valort*0.05)
print('0 corretor'+no+'recebeu'+salario)
