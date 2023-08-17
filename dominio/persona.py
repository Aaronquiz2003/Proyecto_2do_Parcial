# Murillo Santos Joseph
# Quizhpi Aviles Aaron
# Cmpoverde Yong Esthela
# Olvera Herrera Shirley
# Michael Villacis Bohorquez
class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, estatura,
                 fecha_nacimiento,peso,edad,mediana,moda):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._estatura = estatura
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._estatura = estatura
        self._fecha_nacimiento = fecha_nacimiento
        self._peso = peso
        self._edad = edad
        self._mediana = mediana
        self._moda = moda

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, value):
        self._numero_libros = value

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = value

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, value):
        self._carrera = value

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, value):
        self._estatura = value

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value

    @property
    def peso (self):
        return self._peso

    @peso.setter
    def peso(self,value):
        self._peso = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    #@property
    #def media(self):
     #   return self._media
    #@media.setter
    #def media(self,value):
        self._media = value

    #@property
    #def moda (self):
      #  return self._moda
    #@moda.setter
    #def moda (self,value):
     #   self._media=value


    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True

#    def __str__(self):
 #       return f'Persona: [Nombre: {self._nombre} {self._apellido}, Cedula: {self._cedula}]'
