from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog
from PyQt5 import uic

'''
Desarrolle un programa que permita seleccionar, agregar, editar, quitar y quitar todos los elementos
de una lista desplegable. Para las acciones de agregar y editar el usuario ingresa el texto con QinputDialog. 
Para las acciones de quitar y quitar todos emplear QMessageBox para preguntar si el usuario quiere realizar la acción.
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_siete.ui", self)
        self.btnAgregar.clicked.connect(self.al_clic_agregar)
        self.btnEditar.clicked.connect(self.al_clic_editar)
        self.btnQuitar.clicked.connect(self.al_clic_quitar)
        self.btnQuitarTodos.clicked.connect(self.al_clic_quitar_todos)

    def al_clic_agregar(self):
        texto, okPressed = QInputDialog.getText(self, "Agregar item", "Nombre ")
        if okPressed and texto != '':
            self.opciones.addItem(texto)

    def al_clic_editar(self):
        indice = self.opciones.currentIndex()
        texto, okPressed = QInputDialog.getText(self, "Editar item", "Ingresa nuevo nombre ")
        if okPressed and texto != '':
            self.opciones.removeItem(indice)
            self.opciones.addItem(texto)
        
    def al_clic_quitar(self):
        indice = self.opciones.currentIndex()
        #mensaje = QMessageBox()
        #mensaje.setIcon(QMessageBox.Question)
        #mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #mensaje.setWindowTitle("Eliminar item")
        #mensaje.setText("Desea eliminar?")
        #mensaje.exec()
        self.opciones.removeItem(indice)
        
    
    def al_clic_quitar_todos(self):
        self.opciones.clear()
        resultado = QMessageBox()
        resultado.setIcon(QMessageBox.Warning)
        resultado.setWindowTitle("Limpiar todo")
        resultado.setText("Se eliminaron todos los items")
        resultado.exec()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()