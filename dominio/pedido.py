#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley
from libro import Libro
from revista import Revista
from estudiante import Estudiante
from docente import Docente
class Pedido:
    contador_pedido = 0

    def __init__(self, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion):
        self.id = Pedido.contador_pedido + 1
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._materia = materia
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        Pedido.contador_pedido += 1

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, value):
        self._solicitante = value

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, value):
        self._lista_material = value

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, value):
        self._materia = value

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, value):
        self._fecha_prestamo = value

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, value):
        self._fecha_devolucion = value

    def pedir_material(self, list_materia, solicitante, materia):
        self._lista_material = list_materia
        self._solicitante = solicitante
        self._materia = materia

    def devolver_material(self, solicitante):
        self._solicitante = solicitante

    def mostrar_pedido(self):
        pass


# Ejemplo de uso
libro = Libro("123", "Autor", "Título Libro", 2021, "Editorial", True, 5, "Tapa dura")
revista = Revista("456", "Autor", "Título Revista", 2021, "Editorial", False, 3, "Digital")

estudiante = Estudiante("1234567890", "Juan", "Pérez", "juan@example.com", "123456789", "Dirección", 2, True, "Informática", "3er Nivel")
docente = Docente("0987654321", "María", "Gómez", "maria@example.com", "987654321", "Dirección", 3, True, "Matemáticas", "Ph.D.", "M.Sc.")

pedido = Pedido(estudiante, libro, "Programación", "2023-06-11", "2023-06-18")
