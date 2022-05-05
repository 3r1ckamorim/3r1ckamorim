from math import radians, sin, cos, tan
angulo=float(input('qual o grau:'))
m=cos(radians(angulo))
n=sin(radians(angulo))
b=tan(radians(angulo))
print('seno {:.2f}, cosseno {:.2f}, tangente{:.2f}.'.format(n,m,b))