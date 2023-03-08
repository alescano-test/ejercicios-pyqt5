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

#!-----------------------------------------------------------------------------------------------------
    def editar_persona(self):
        fila = self.tablaDatos.currentRow()
        colum = self.tablaDatos.currentColumn()

        #? Nombre
        if colum == 0:
            texto, ok = QInputDialog.getText(self, "Editar", "Nuevo nombre")
            if ok and texto != '':
                self.tablaDatos.setItem(fila, colum, QTableWidgetItem(texto))
            else:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el nombre")
                msg.exec()
        #? Apellido
        if colum == 1:
            texto, ok = QInputDialog.getText(self, "Editar", "Nuevo apellido")
            if ok and texto != '':
                self.tablaDatos.setItem(fila, colum, QTableWidgetItem(texto))
            else:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el nombre")
                msg.exec()
        #? Email
        if colum == 2:
            texto, ok = QInputDialog.getText(self, "Editar", "Nuevo email")
            if ok and texto != '':
                self.tablaDatos.setItem(fila, colum, QTableWidgetItem(texto))
            else:
                msg = QMessageBox(QMessageBox.Warning, "Error", "Tienes que completar el nombre")
                msg.exec()

#!-----------------------------------------------------------------------------------------------------
    def eliminar_persona(self):
        msg = QMessageBox(QMessageBox.Warning, "Eliminar", "Seguro quieres eliminarlo?", QMessageBox.Yes | QMessageBox.No)
        resultado = msg.exec()
        if resultado == QMessageBox.Yes: 
            fila = self.tablaDatos.currentRow()
            self.tablaDatos.removeRow(fila)
        if resultado == QMessageBox.No:
            pass

#!-----------------------------------------------------------------------------------------------------
    def borrar_entradas(self):
        self.nombre.clear()
        self.apellido.clear()
        self.email.clear()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()