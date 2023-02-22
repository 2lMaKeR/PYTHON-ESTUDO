# diaria=60 / km=0.15
# dias alugados + km percorridos = total
dia=int(input('por quantos dias foi alugado o veículo:'))
km=float(input('quantos kilômetros foram percorridos com o veículo:'))
diar=(dia*60)
kms=(km*0.15)
tot=(diar+kms)
print('total a pagar R{}.'.format(tot))