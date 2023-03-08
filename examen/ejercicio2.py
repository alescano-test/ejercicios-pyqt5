from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QInputDialog
import csv
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("examen/ejercicio_dos.ui", self)
        self.btnAgregar.clicked.connect(self.on_clicked_agregar)


    def on_clicked_agregar(self):
            if len(self.nombre.text()) == 0:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el nombre")
                msg.exec()
            if len(self.apellido.text()) == 0:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el apellido")
                msg.exec()
            if len(self.email.text()) == 0:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el email")
                msg.exec()
            if len(self.nombre.text()) and len(self.apellido.text()) and len(self.email.text()) != 0:
                self.tablaDatos.insertRow(0)
                self.tablaDatos.setItem(0, 0, QTableWidgetItem(self.nombre.text()))
                self.tablaDatos.setItem(0, 1, QTableWidgetItem(self.apellido.text()))
                self.tablaDatos.setItem(0, 2, QTableWidgetItem(self.email.text()))
                self.borrar_entradas()

    def borrar_entradas(self):
        self.nombre.clear()
        self.apellido.clear()
        self.email.clear()
    
    def guardar_csv(self):
         pass

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()