class Restaurante: # - class sempre com letra maiúscula como Restaurante
    def __initi__(self,nome,categoria):
        self.nome=''
        self.categoria=''
        self.ativo=False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome}|{restaurante.categoria}|{restaurante.ativo}')

restaurante_plaza=Restaurante('Plaza','Gourmet')
restaurante_pizza=Restaurante('Pizza Suprema','Italiana')

Restaurante.listar_restaurantes()
