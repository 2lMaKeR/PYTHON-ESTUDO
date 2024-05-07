class Restaurante: # - class sempre com letra maiúscula como Restaurante
    restaurantes=[]

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._ativo=False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(20)}|{'Categoria'.ljust(20)}|{'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)}|{restaurante.categoria.ljust(20)}|{restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo=not self._ativo

restaurante_plaza=Restaurante('plaza','Gourmet')
restaurante_pizza=Restaurante('pizza suprema','Italiana')

Restaurante.listar_restaurantes()
