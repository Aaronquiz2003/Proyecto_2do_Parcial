#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley

from datetime import date
from pedido import Pedido
class Material:
    contador_libro = 0
    contador_revista = 0

    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.anio = anio
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad_disponible = cantidad_disponible

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible

class Libro(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo_pasta):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id = Material.contador_libro + 1
        self.tipo_pasta = tipo_pasta
        Material.contador_libro += 1

    def get_titulo(self):
        return self.titulo

class Revista(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id = Material.contador_revista + 1
        self.tipo = tipo
        Material.contador_revista += 1

class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.numero_libros = numero_libros
        self.activo = activo
        self.carrera = carrera

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True

    def __str__(self):
        return f'Persona: [Nombre: {self.nombre} {self.apellido}, Cedula: {self.cedula}]'


class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id = Estudiante.contador_estudiante + 1
        self.nivel = nivel
        Estudiante.contador_estudiante += 1


class Docente(Persona):
    contador_docente = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,
                 titulo_3er_nivel, titulo_4to_nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id = Docente.contador_docente + 1
        self.titulo_3er_nivel = titulo_3er_nivel
        self.titulo_4to_nivel = titulo_4to_nivel
        Docente.contador_docente += 1

class Pedido:
    contador_pedido = 0

    def __init__(self, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion):
        self.id = Pedido.contador_pedido + 1
        self.solicitante = solicitante
        self.lista_material = lista_material
        self.materia = materia
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        Pedido.contador_pedido += 1

    def pedir_material(self, lista_material, solicitante, materia):
        self.lista_material = lista_material
        self.solicitante = solicitante
        self.materia = materia

    def devolver_material(self, solicitante):
        self.solicitante = solicitante

# Ejemplo de uso
libro = Libro("123", "Autor", "Diario de Anna Frank", 2021, "Editorial", True, 5, "Tapa dura")
revista = Revista("456", "Autor", "Televistazo", 2021, "Editorial", False, 3, "Digital")

estudiante = Estudiante("1234567890", "Juan", "Pérez", "juan@example.com", "123456789", "Dirección", 2, True, "Informática", "3er Nivel")
docente = Docente("0987654321", "María", "Gómez", "maria@example.com", "987654321", "Dirección", 3, True, "Matemáticas", "Ph.D.", "M.Sc.")

fecha_prestamo = date.today()
fecha_devolucion = fecha_prestamo.replace(day=fecha_prestamo.day+7)  # Devolución en 7 días

pedido = Pedido(estudiante, libro, "Programación", fecha_prestamo, fecha_devolucion)
print("/////////////////////////////////////////////////////////////")
print("|      TITULO DEL LIBRO: ",libro.titulo,)  # Salida: Título Libro
print("|      FECHA DE PRESTAMO: ",fecha_prestamo,)
print("|      NOMBRE DE REVISTA: ",revista.titulo )# Salida: Título Revista
print("|      ESTUDIANTE: ",estudiante.nombre,                    "|")  # Salida: Juan
print("|      DOCENTE: ",docente.nombre,                          "|")  # Salida: María
print("|      NOMBRE DEL QUE PIDIDO: ",pedido.solicitante.nombre, "|")  # Salida: Juan
print("|      PEDIDO DE: ",pedido.lista_material.titulo,          "|")  # Salida: Título Libro
print("|      FECHA DE DEVOLUCION: ",fecha_devolucion,            "|")
print("/////////////////////////////////////////////////////////////")

