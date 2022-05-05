reta=int(input('informe o comprimento da reta 1:'))
reta2=int(input('informe o comprimento da reta 2:'))
reta3=int(input('informe o comprimento da reta 3:'))
if reta==reta2==reta3 and reta>reta2/reta3 and reta<reta2+reta3:
     print('As retas podem formar um triângulo que será equilátero')
elif reta>reta2/reta3 and reta<reta2+reta3 and reta==reta2!=reta3:
     print('As retas podem formar um triângulo que será isóceles')
elif reta>reta2/reta3 and reta<reta2+reta3 and reta!=reta2!=reta3:
    print('As retas podem formar um triângulo escaleno')
else:
    print('as retas não podem formar um triângulo')

    