from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_ocho.ui", self)
        self.moverDerecha.clicked.connect(self.mover_derecha)
        self.moverIzquierda.clicked.connect(self.mover_izquierda)

    def mover_derecha(self):
        fila = self.listaIzquierda.currentRow()
        itemActual = self.listaIzquierda.currentItem()
        self.listaDerecha.insertItem(0, itemActual.text())
        self.listaIzquierda.takeItem(fila)
        if self.listaIzquierda.count() < 1:
            self.moverDerecha.setEnabled(False)
            self.moverIzquierda.setEnabled(True)
        else:
            self.moverDerecha.setEnabled(True)
            self.moverIzquierda.setEnabled(True)

    def mover_izquierda(self):
        fila = self.listaDerecha.currentRow()
        itemActual = self.listaDerecha.currentItem()
        self.listaIzquierda.insertItem(0, itemActual.text())
        self.listaDerecha.takeItem(fila)

        if self.listaDerecha.count() < 1:
            self.moverDerecha.setEnabled(True)
            self.moverIzquierda.setEnabled(False)
        else:
            self.moverDerecha.setEnabled(True)
            self.moverIzquierda.setEnabled(True)


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
