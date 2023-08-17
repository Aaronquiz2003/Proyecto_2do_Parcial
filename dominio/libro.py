#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley
from material import Material
class Libro(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo_pasta):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id = Material.contador_libro + 1
        self._tipo_pasta = tipo_pasta
        Material.contador_libro += 1

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, value):
        self._tipo_pasta = value

    def get_titulo(self):
        return self._titulo