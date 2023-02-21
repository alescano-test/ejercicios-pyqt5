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
        if self.nombre.text() and self.apellido.text() and self.email.text() != '':
            self.tablaDatos.insertRow(0)
            self.tablaDatos.setItem(0, 0, QTableWidgetItem(self.nombre.text()))
            self.tablaDatos.setItem(0, 1, QTableWidgetItem(self.apellido.text()))
            self.tablaDatos.setItem(0, 2, QTableWidgetItem(self.email.text()))
            self.borrar_entradas() 
        else:
            msg = QMessageBox(QMessageBox.Warning, "Error", "Todos los campos están vacíos.")
            msg.exec()

    def editar_persona(self):
        fila = self.tablaDatos.currentRow()
        #self.nombre.setText(self.tablaDatos.item(fila ,0).text())
        #self.apellido.setText(self.tablaDatos.item(fila ,1).text())
        #self.email.setText(self.tablaDatos.item(fila ,2).text())
        for i in range(2):
            if i == 0:
                texto, ok = QInputDialog.getText(self, "Nombre", "Ingresar el nuevo nombre:")
                if ok and texto != '':
                    self.tablaDatos.setItem(fila, i, QTableWidgetItem(texto))
                else:
                    msg = QMessageBox(QMessageBox.Warning, "Error", "Por favor, ingrese el nombre.")
                    msg.exec()
            if i == 1:
                texto, ok = QInputDialog.getText(self, "Nombre", "Ingresar el nuevo nombre:")
                if ok and texto != '':
                    self.tablaDatos.setItem(fila, i, QTableWidgetItem(texto))
                    msg = QMessageBox(QMessageBox.Warning, "Error", "Por favor, ingrese el apellido.")
                    msg.exec()
            if i == 2:
                texto, ok = QInputDialog.getText(self, "Nombre", "Ingresar el nuevo email:")
                if ok and texto != '':
                    self.tablaDatos.setItem(fila, i, QTableWidgetItem(texto))
                    msg = QMessageBox(QMessageBox.Warning, "Error", "Por favor, ingrese el email.")
                    msg.exec()
            




    def eliminar_persona(self):
        fila = self.tablaDatos.currentRow()
        self.tablaDatos.removeRow(fila)
        self.borrar_entradas()

    def borrar_entradas(self):
        self.nombre.clear()
        self.apellido.clear()
        self.email.clear()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()