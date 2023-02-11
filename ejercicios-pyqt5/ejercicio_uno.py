from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

'''
Desarrollar un programa que al hacer clic en el botón
cambie el texto de la etiqueta a “Chau mundo!”
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/ejercicio_uno.ui", self)
        self.boton.clicked.connect(self.cambiarSaludo)
    
    def cambiarSaludo(self):
        if self.mensaje.text() == "Hola mundo!":
            self.mensaje.setText("Chau mundo!")
        else:
            self.mensaje.setText("Hola mundo!")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()