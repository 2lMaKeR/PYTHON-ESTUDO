# importando modulos
import math
import random

# -- -- --

num=float(input('digite um número: '))
numI=(math.floor(num)) #também nesse ex pode ser usado "trunc" para cortar a parte inteira do num
print('o número {} possui o número inteiro de {} dentro de si.'.format(num,numI))

# -- -- --

catop=float(input('qual o comprimento do cateto oposto:'))
catad=float(input('qual o comprimento do cateto adjacente:'))
# hipo=(((catop**2)+(catad**2))**(1/2)) # no padrão matematico
hipo=math.hypot(catop, catad) # usando math
print(' a hipotenusa é {}'.format(hipo))

# -- -- --

ang=float(input('digite um ângulo: '))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print('o ângulo de{} graus possui o seno de {:.3f}, o cosseno de {:.3f} e a tangente de {:.3f}.'.format(ang,sen,cos,tan))

# -- -- --

print('Bem-vindo ao aleatorizador de lanchinhos, digite suas opções abaixo.')
l1=str(input('opção 1: '))
l2=str(input('opção 2: '))
l3=str(input('opção 3: '))
l4=str(input('opção 4: '))
li=l1,l2,l3,l4
choice=random.choice(li)
print('o lanchinho escolhido foi {}, tenho um bom lanche!!'.format(choice))

# -- -- --

print('Bem-vindo ao randomizador de 5x5, digite o nome dos participantes abaixo.')
p1=str(input('player 1: '))
p2=str(input('player 2: '))
p3=str(input('player 3: '))
p4=str(input('player 4: '))
p5=str(input('player 5: '))
p6=str(input('player 6: '))
p7=str(input('player 7: '))
p8=str(input('player 8: '))
p9=str(input('player 9: '))
p10=str(input('player 10: '))
lista=[p1,p2,p3,p4,p5,p6,p7,p8,p9,10]
party=random.shuffle(lista)
print('time 1 composto pelos 5 primeiros players, o restante será o time 2.')
print(lista)

# -- -- --

