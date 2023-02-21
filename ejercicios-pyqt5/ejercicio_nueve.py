from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic

'''
Realizar un programa que permita agregar, editar y quitar personas de una tabla con
nombre, apellido y email de personas.
'''
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_nueve.ui", self)
        self.btnAgregar.clicked.connect(self.agregar_persona)
        self.btnEditar.clicked.connect(self.editar_persona)
        self.btnEliminar.clicked.connect(self.eliminar_persona)

    def agregar_persona(self):
        self.tablaDatos.insertRow(0)
        self.tablaDatos.setItem(0, 0, QTableWidgetItem(self.nombre.text()))
        self.tablaDatos.setItem(0, 1, QTableWidgetItem(self.apellido.text()))
        self.tablaDatos.setItem(0, 2, QTableWidgetItem(self.email.text()))
        self.borrar_entradas() 

    def editar_persona(self):
        fila = self.tablaDatos.currentRow()
        self.nombre.setText(self.tablaDatos.item(fila ,0).text())
        self.apellido.setText(self.tablaDatos.item(fila ,1).text())
        self.email.setText(self.tablaDatos.item(fila ,2).text())
        #self.tablaDatos.item()

    def eliminar_persona(self):
        fila = self.tablaDatos.currentRow()
        self.tablaDatos.removeRow(fila)

    def borrar_entradas(self):
        self.nombre.clear()
        self.apellido.clear()
        self.email.clear()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()