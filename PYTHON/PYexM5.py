#style = 0(none), 1(bold), 4(underline), 7(negative)
#text = 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(ciano), 37(cinza)
#back = 40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(ciano), 47(cinza)

#\033[0;33;44m

print('\33[4;30;45mOlá mundo!\33[m')
a=1
b=3
print('números \33[32m{}\33[m e \33[31m{}\33[m.'.format(a,b))

# -- -- -- 

nome='Felipe'
cores={'limpa':'\33[m',
       'azul':'\33[34m',
       'amarelo':'\33[33m',
       'pretoebranco':'\33[7;30m',}
print('pega a visão {}{}{} nessa parada!'.format(cores['amarelo'],nome,cores['limpa']))
