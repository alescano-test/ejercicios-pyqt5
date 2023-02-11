from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

'''
Teniendo en cuenta la siguiente interfaz,
desarrollar un programa que permita ingresar el nombre y
apellido de una persona y al hacer clic en ‘mostrar’ se
modifique el texto de la etiqueta con el apellido y nombre
cargado separado por coma.
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/ejercicio_tres.ui", self)
        self.mostrar.clicked.connect(self.mostrarNombre)
    
    def mostrarNombre(self):
        self.nom_compl.setText(f"{self.nombre.text()}, {self.apellido.text()}")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()