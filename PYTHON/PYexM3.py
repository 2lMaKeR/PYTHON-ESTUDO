frase = 'curso em video python'
print(frase.upper()[3:13:2])
print("""print infinito""")#colocando tres aspas duplas

# -- -- --

fr=str(input('digite seu nome: ')).strip()
frs=fr.upper()
frl=fr.lower()
frt=len(fr)
fr1n=fr.find(' ')
sr=fr.split()
print('seu nome é forte assim {}!! também podendo ser {} bem stealth...\n assim seu nome possuindo {} letras e seu primeiro nome possuindo {} letras.'.format(frs,frl,frt,fr1n))
print('seu primeiro nome {} tem {} letras'.format(sr[0],len(sr[0])))# guanabara feels

# -- -- --

num=int(input('digite um número: '))
und=num//1%10
dez=num//10%10
cent=num//100%10
mlh=num//1000%10
print('este número possui {} unidade(s), {} dezena(s), {} centena(s) e {} unidade(s) de milhar.'.format(und,dez,cent,mlh))

# -- -- --

mun=str(input('digite uma cidade com "santo" no nome: '))
print(mun[:5].upper()=='SANTO')

# -- -- --

nome=str(input('qual é seu nome completo: ')).strip()
print('seu nome tem silva? {}'.format('silva' in nome.lower()))

# -- -- --

frase=str(input('digite uma frase: ')).strip().upper()
print('a letra "a" aparece {} vezes dentro desta frase, aparecendo a primeira vez na posição {} e a ultima vez na posição {}.'
      .format((frase.count('A')),(frase.find('A')+1),(frase.rfind('A')+1)))

# -- -- --

name=str(input('digite seu nome completo: ')).strip()
name2=name.split()
print('muito prazer em te conhecer {}, da familia {}!!'.format((name2[0]),(name2[len(name2)-1])))
