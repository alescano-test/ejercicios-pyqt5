from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("examen/ejercicio_uno.ui", self)
        self.agregar.clicked.connect(self.on_clicked_agregar)
        self.quitarA.clicked.connect(self.on_clicked_quitarA)
        self.quitarB.clicked.connect(self.on_clicked_quitarB)
    
    def on_clicked_agregar(self):
        elemento = self.inputElemento.text()
        if len(elemento) > 1:
            if self.chA.isChecked() == True:
                self.listaA.insertItem(0, elemento)
            if self.chB.isChecked() == True:
                self.listaB.insertItem(0, elemento)
        else:
            msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el elemento.")
            msg.exec()
        
    
    def on_clicked_quitarA(self):
        fila = self.listaA.currentRow()
        self.listaA.takeItem(fila)
    
    def on_clicked_quitarB(self):
        fila = self.listaB.currentRow()
        self.listaB.takeItem(fila)

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()