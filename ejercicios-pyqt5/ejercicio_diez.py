from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

'''
Desarrollar un programa que al hacer clic en el botón
cambie el texto de la etiqueta a “Chau mundo!”
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_diez.ui", self)


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()