from datetime import date

# -- -- --

num=int(input('digite um número: '))
res=(num%2)
if res==0:
    print('o número {} é par.'.format(num))
else:
    print('o número {} é impar.'.format(num))

# -- -- --

dist=float(input('qual é a distância da sua viagem: '))
val=dist*0.5 if dist<=200 else dist *0.45
print('para a distância de {}Km, sua passagem será do valor de R${:.2f}.'.format(dist,val))

# -- -- --

ano=int(input('Analise de ano bissextais: '))
if ano == 0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('o ano {} é bissexto.'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))

# -- -- -- 

n1=int(input('primeiro número: '))
n2=int(input('segundo número: '))
n3=int(input('terceiro número: '))
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('o menor número digitado foi {}.'.format(menor))
print('o maior número digitado foi {}.'.format(maior))

# -- -- --

sal=float(input('qual o salário do funcionário que sofrerá aumento? R$: '))
if sal <= 1302:
    novo=sal+(sal*0.15)
else:
    novo=sal+(sal*0.1)
print('agora terá o salário atual de R${:.2f}.'.format(novo))

# -- -- -- 

print('Digite os lados do triângulo')
l1=float(input('primeiro lado: '))
l2=float(input('segundo lado: '))
l3=float(input('terceiro lado: '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('os lados acima formam um triângulo.')
else:
    print('os lados não formam um triângulo.')

# -- -- -- 