reta=int(input('informe o comprimento da reta 1:'))
reta2=int(input('informe o comprimento da reta 2:'))
reta3=int(input('informe o comprimento da reta 3:'))
if reta>reta2/reta3 and reta<reta2+reta3:
    print('As retas podem formar um triângulo')
else:
    print('as retas não podem formar um triângulo')