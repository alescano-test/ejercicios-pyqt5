from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

'''
Realizar un programa que al iniciarse deshabilite todos los botones a excepción
del botón ‘arriba’. Luego al hacer clic en el botón ‘arriba’ se habilite el botón ‘derecha’ y deshabilite el botón ‘arriba’.
Repetir la secuencia siguiendo el sentido de las agujas del reloj.
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/ejercicio_dos.ui", self)
        self.arriba.clicked.connect(self.clickArriba)
        self.derecha.clicked.connect(self.clickDerecha)
        self.abajo.clicked.connect(self.clickAbajo)
        self.izquierda.clicked.connect(self.clickIzquierda)

    def clickArriba(self):
            self.arriba.setEnabled(False)
            self.derecha.setEnabled(True)
            self.abajo.setEnabled(False)
            self.izquierda.setEnabled(False)
    def clickDerecha(self):
            self.arriba.setEnabled(False)
            self.derecha.setEnabled(False)
            self.abajo.setEnabled(True)
            self.izquierda.setEnabled(False)
    def clickAbajo(self):
            self.arriba.setEnabled(False)
            self.derecha.setEnabled(False)
            self.abajo.setEnabled(False)
            self.izquierda.setEnabled(True)
    def clickIzquierda(self):
            self.arriba.setEnabled(True)
            self.derecha.setEnabled(False)
            self.abajo.setEnabled(False)
            self.izquierda.setEnabled(False)


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()