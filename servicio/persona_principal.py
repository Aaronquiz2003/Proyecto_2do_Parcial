from datetime import datetime

from PySide6 import QtGui, QtCore
from PySide6.QtCore import QDate
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from Datos.estudiante_dao import EstudianteDao
from UI.vtn_principal import Ui_vtn_principal
from dominio.docente import Docente
from dominio.estudiante import Estudiante

class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        self.ui.vtn_grabar.clicked.connect(self.grabar)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        self.ui.vtn_calcular.clicked.connect(self.calculos_edad)
        self.ui.vtn_calcular.clicked.connect(self.calculos_estatura)
        self.ui.vtn_calcular.clicked.connect(self.calculos_peso)
        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if (self.ui.txt_nombre.text() == '' or self.ui.txt_apellido.text() == '' or len(self.ui.txt_cedula.text()) < 10
                or self.ui.txt_email.text() == ''):
            print('Completar datos')
            QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios.')
        else:
            persona = None
            if tipo_persona == 'Docente':
                persona = Docente()
                persona.cedula = self.ui.txt_cedula.text()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.fecha_nacimiento = self.ui.date_f_nacimiento.date().toString(QtCore.Qt.ISODate)
                persona.estatura = float(self.ui.sp_estatura.value())
                persona.peso = float(self.ui.sp_peso.value())
            else:
                persona = Estudiante()
                persona.cedula = self.ui.txt_cedula.text()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.fecha_nacimiento = self.ui.date_f_nacimiento.date().toString(QtCore.Qt.ISODate)
                persona.estatura = float(self.ui.sp_estatura.value())
                persona.peso = float(self.ui.sp_peso.value())

            respuesta = EstudianteDao.insertar_estudiante(persona)
            print(respuesta)
            if respuesta['exito']:
                self.ui.txt_nombre.setText('')
                self.ui.txt_apellido.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.txt_email.setText('')
                self.ui.txt_carrera.setText('')
                self.ui.sp_estatura.setValue(0)
                self.ui.date_f_nacimiento.setDate(QtCore.QDate())
                self.ui.sp_peso.setValue(0)
                self.ui.stb_estado.showMessage('Grabado con éxito.', 2000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])

        print("----------PARTICIPANTES DEL GRUPO # 8-------------")
        print("-  Murillo Santos Joseph "
              "\n-  Quizhpi Aviles Aaron"
              "\n-  Villacis Bohorquez Michael "
              "\n-  Campoverde Yong Esthela"
              "\n-  Olvera Herrera Shirley")
    def buscar_x_cedula(self):
        cedula = self.ui.txt_cedula.text()
        e = Estudiante(cedula=cedula)
        e = EstudianteDao.seleccionar_por_cedula(e)

        print(e)
        self.ui.txt_nombre.setText(e.nombre)
        self.ui.txt_apellido.setText(e.apellido)
        self.ui.txt_email.setText(e.email)
        self.ui.txt_carrera.setText(e.carrera)
        self.ui.cb_tipo_persona.setCurrentText('Estudiante')
        self.ui.sp_estatura.setValue(e.estatura)
        fecha_nacimiento = e.fecha_nacimiento
        year = fecha_nacimiento.year
        month = fecha_nacimiento.month
        day = fecha_nacimiento.day
        self.ui.date_f_nacimiento.setDate(QDate(year, month, day))
        self.ui.sp_peso.setValue(e.peso)
        print("----------PARTICIPANTES DEL GRUPO # 8-------------")
        print("-  Murillo Santos Joseph "
              "\n-  Quizhpi Aviles Aaron"
              "\n-  Villacis Bohorquez Michael "
              "\n-  Campoverde Yong Esthela"
              "\n-  Olvera Herrera Shirley")
    def calculos_estatura(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        estaturas = [estudiante.estatura for estudiante in estudiantes if estudiante.estatura is not None]
        if len(estaturas) == 0:
            print('No hay estaturas válidas para calcular la moda, mediana, máximo y mínimo.')
            return
        moda = max(set(estaturas), key=estaturas.count)
        mediana = sorted(estaturas)[len(estaturas) // 2]
        maximo = max(estaturas)
        minimo = min(estaturas)
        media_estatura = sum(estaturas) / len(estaturas)

        print("\n---------- CALCULOS DE ESTATURA -------------")
        print(f'- La moda de estaturas es     : {moda}')
        print(f'- La mediana de estaturas es  : {mediana}')
        print(f'- El máximo de estaturas es   : {maximo}')
        print(f'- El mínimo de estaturas es   : {minimo}')
        print(f'- La media de estaturas es    : {media_estatura:,.2f}')

    def calculos_peso(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        pesos = [estudiante.peso for estudiante in estudiantes if estudiante.peso is not None]
        if len(pesos) == 0:
            print('No hay pesos válidos para calcular la moda, mediana, máximo y mínimo.')
            return
        moda = max(set(pesos), key=pesos.count)
        mediana = sorted(pesos)[len(pesos) // 2]
        maximo = max(pesos)
        minimo = min(pesos)
        media_peso = sum(pesos) / len(pesos)
        print("\n---------- CALCULOS DE PESO -------------")
        print(f'- La moda de pesos es     : {moda}')
        print(f'- La mediana de pesos es  : {mediana}')
        print(f'- El máximo de pesos es   : {maximo}')
        print(f'- El mínimo de pesos es   : {minimo}')
        print(f'- La media de pesos es    : {media_peso:,.2f}')
    def calculos_edad(self):
        edades = EstudianteDao.obtener_edades_todos_estudiantes()

        if edades is None or len(edades) == 0:
            print("No se obtuvieron edades.")
            return
        suma_edades = sum(edades)
        cantidad_edades = len(edades)
        if cantidad_edades == 0:
            print("No hay edades para calcular promedio.")
            return
        promedio_edades = suma_edades / cantidad_edades
        if len(edades) > 1:
            moda_edades = max(set(edades), key=edades.count)
            mediana_edades = sorted(edades)[len(edades) // 2]
        else:
            moda_edades = edades[0]
            mediana_edades = edades[0]

        maximo_edades = max(edades)
        minimo_edades = min(edades)
        print("----------PARTICIPANTES DEL GRUPO # 8-------------")
        print("-  Murillo Santos Joseph "
              "\n-  Quizhpi Aviles Aaron"
              "\n-  Villacis Bohorquez Michael "
              "\n-  Campoverde Yong Esthela"
              "\n-  Olvera Herrera Shirley")

        print("\n---------- CALCULOS DE EDAD -------------")
        print(f'- La moda de edades    : {moda_edades}')
        print(f'- La mediana de edades : {mediana_edades}')
        print(f'- Total de edades      : {suma_edades}')
        print(f'- El máximo de edades  : {maximo_edades}')
        print(f'- El mínimo de edades  : {minimo_edades}')
        print(f'- La media de edades   : {promedio_edades:,.2f}')

