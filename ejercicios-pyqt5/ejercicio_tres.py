from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

'''
Desarrollar un programa que permita ingresar el nombre y apellido de una persona
y al hacer clic en ‘mostrar’ se modifique el texto de la etiqueta con el apellido 
y nombre cargado separado por coma.
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_tres.ui", self)
        self.mostrar.clicked.connect(self.mostrarNombre)

    
    def mostrarNombre(self):
        lenNombre = self.nombre.text()
        lenApellido = self.apellido.text()
        if len(lenNombre) == 0:
            msg = QMessageBox(QMessageBox.Warning, "Error", "El nombre es requerido.")
            msg.exec()
        if len(lenApellido) == 0:
            msg = QMessageBox(QMessageBox.Warning, "Error", "El apellido es requerido.")
            msg.exec()
        if len(lenApellido) and len(lenApellido) >= 1:
            self.nom_compl.setText(f"{lenNombre}, {lenApellido}")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()