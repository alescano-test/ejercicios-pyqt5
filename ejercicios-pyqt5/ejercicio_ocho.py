from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_ocho.ui", self)
        #self.listaIzquierda.currentRowChanged.connect(self.mover_izquierda)
        #self.listaDerecha.currentRowChanged.connect(self.mover_derecha)
        self.moverIzquierda.clicked.connect(self.mover_izquierda)
        self.moverDerecha.clicked.connect(self.mover_derecha)
    
    def mover_izquierda(self):
        item = self.listaDerecha.currentItem()
        fila = self.listaDerecha.currentRow()
        cant_items = self.listaDerecha.count()
        self.listaIzquierda.insertItem(0, item.text())
        self.listaDerecha.takeItem(fila)
        if cant_items == 0:
            self.moverIzquierda.setEnabled(False)
        else:
            self.moverIzquierda.setEnabled(True)

    def mover_derecha(self):
        item = self.listaIzquierda.currentItem()
        fila = self.listaIzquierda.currentRow()
        cant_items = self.listaIzquierda.count()
        self.listaDerecha.insertItem(0, item.text())
        self.listaIzquierda.takeItem(fila)
        if cant_items == 0:
            self.moverDerecha.setEnabled(False)
        else:
            self.moverDerecha.setEnabled(True)        

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
        