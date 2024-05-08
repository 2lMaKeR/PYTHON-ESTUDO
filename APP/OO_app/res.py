from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_plaza=Restaurante('plaza','gourmet')
restaurante_mexicano=Restaurante('Arriba','Mexicano')
restaurante_japones=Restaurante('JapaCama','Japonesa')
bebida_moscow_mule=Bebida('Moscow Mule',25,'pequeno')
prato_coxinha=Prato('Coxinha',7,'O Melhor petisco do mundo')

def main():
    print(bebida_moscow_mule)
    print(prato_coxinha)

if __name__=='__main__':
    main()