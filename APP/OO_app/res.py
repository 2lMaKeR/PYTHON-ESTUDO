from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_plaza=Restaurante('plaza','gourmet')
restaurante_mexicano=Restaurante('Arriba','Mexicano')
restaurante_japones=Restaurante('JapaCama','Japonesa')

bebida_moscow_mule=Bebida('Moscow Mule',25,'Pequeno')

prato_coxinha=Prato('Coxinha',7,'O Melhor petisco do mundo')

restaurante_plaza.adicionar_no_cardapio(bebida_moscow_mule)
restaurante_plaza.adicionar_no_cardapio(prato_coxinha)

def main():
    restaurante_plaza.exibir_cardapio

if __name__=='__main__':
    main()