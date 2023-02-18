from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_ocho.ui", self)
        self.moverIzquierda.clicked.connect(self.mover_izquierda)
        self.moverDerecha.clicked.connect(self.mover_derecha)
    

    def mover_izquierda(self):
        cant_items = self.listaDerecha.count()
        item = self.listaDerecha.currentItem()
        fila = self.listaDerecha.currentRow()
        self.listaIzquierda.insertItem(0, item.text())
        self.listaDerecha.takeItem(fila)
        if cant_items <= 0:
            self.moverIzquierda.setEnabled(False)
            self.moverDerecha.setEnabled(True)
        else:
            self.moverIzquierda.setEnabled(False)
            self.moverDerecha.setEnabled(True)


    def mover_derecha(self):
        cant_items = self.listaIzquierda.count()
        item = self.listaIzquierda.currentItem()
        fila = self.listaIzquierda.currentRow()
        self.moverDerecha.setEnabled(False)
        self.listaDerecha.insertItem(0, item.text())
        self.listaIzquierda.takeItem(fila)  
        if cant_items <= 0:
            self.moverIzquierda.setEnabled(True)
            self.moverDerecha.setEnabled(False)
        else:
            self.moverIzquierda.setEnabled(True)
            self.moverDerecha.setEnabled(False)

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
        