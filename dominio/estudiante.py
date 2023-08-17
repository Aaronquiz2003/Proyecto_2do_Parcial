#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley
from datetime import datetime

from dominio.persona import Persona
class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula:str=None, nombre:str=None, apellido:str=None, email:str=None, telefono:str=None, direccion:str=None, numero_libros:int=0, activo:bool=True, carrera:str=None, nivel:str=None,estatura:int =0,fecha_nacimiento:datetime=None,peso:int=0,edad:int=None,mediana:int=0,moda:int=0):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,estatura,fecha_nacimiento,peso,edad,mediana,moda)
        self.fecha_nacimiento = fecha_nacimiento
        self.id = Estudiante.contador_estudiante + 1
        self._nivel = nivel
        Estudiante.contador_estudiante += 1

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value):
        self._nivel = value


def lista_estudiantes():
    return None