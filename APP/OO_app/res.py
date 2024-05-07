from modelos.restaurante import Restaurante

restaurante_plaza=Restaurante('plaza','gourmet')
restaurante_mexicano=Restaurante('Arriba','Mexicano')
restaurante_japones=Restaurante('JapaCama','Japonesa')
restaurante_plaza.receber_avaliacao('Gui',8)
restaurante_plaza.receber_avaliacao('Emi',4)
restaurante_japones.receber_avaliacao('Gui',8)
restaurante_japones.receber_avaliacao('Emi',3)

def main():
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()