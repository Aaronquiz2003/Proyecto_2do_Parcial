#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley
from material import Material
class Revista(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id = Material.contador_revista + 1
        self._tipo = tipo
        Material.contador_revista += 1

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value
