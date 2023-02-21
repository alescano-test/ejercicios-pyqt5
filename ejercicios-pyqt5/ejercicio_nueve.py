from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5 import uic

'''
Realizar un programa que permita agregar, editar y quitar personas de una tabla con
nombre, apellido y email de personas.
'''
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_nueve.ui", self)
        self.btnAgregar.clicked.connect(self.agregar_persona)
        self.btnEditar.clicked.connect(self.editar_persona)
        self.btnEliminar.clicked.connect(self.eliminar_persona)

    def agregar_persona(self):
        self.tablaDatos.insertRow(0)
        self.tablaDatos.setItem(0, 0, QTableWidgetItem(self.nombre.text()))
        self.tablaDatos.setItem(0, 1, QTableWidgetItem(self.apellido.text()))
        self.tablaDatos.setItem(0, 2, QTableWidgetItem(self.email.text()))
        self.borrar_entradas() 

    def editar_persona(self):
        fila = self.tablaDatos.currentRow()
        colum = self.tablaDatos.currentColumn()
        if colum == 0:
            texto, ok = QInputDialog.getText(self, "Editar", "Nuevo nombre")
            if ok and texto != '':
                self.tablaDatos.setItem(fila, colum, QTableWidgetItem(texto))
            else:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el nombre")
                msg.exec()
        if colum == 1:
            texto, ok = QInputDialog.getText(self, "Editar", "Nuevo apellido")
            if ok and texto != '':
                self.tablaDatos.setItem(fila, colum, QTableWidgetItem(texto))
            else:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el nombre")
                msg.exec()
        if colum == 2:
            texto, ok = QInputDialog.getText(self, "Editar", "Nuevo email")
            if ok and texto != '':
                self.tablaDatos.setItem(fila, colum, QTableWidgetItem(texto))
            else:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el nombre")
                msg.exec()


        #self.tablaDatos.item()

    def eliminar_persona(self):
        fila = self.tablaDatos.currentRow()
        self.tablaDatos.removeRow(fila)

    def borrar_entradas(self):
        self.nombre.clear()
        self.apellido.clear()
        self.email.clear()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()