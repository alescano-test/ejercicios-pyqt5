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
        self.opciones.currentIndexChanged.connect(self.in_actual)
#!------------------------------------------------------------------------------------------------------
  
    def in_actual(self, ind):
        print(ind)

#!------------------------------------------------------------------------------------------------------

    def al_clic_agregar(self):
        cant_items = self.opciones.count() #* Cantidad de items en el combo box.
        indice = self.opciones.currentIndex() #* El indice del indice en el que estamos posicionados.
        texto, okPressed = QInputDialog.getText(self, "Agregar item", "Nombre: ") #* texto = string que el usuario ingresa en el campo de entrada, si hace clic en el botón "Aceptar" 
                                                                                  #* okPressed = bool, Aceptar = True , Cancelar = False
        #? Si presiona Aceptar y texto es diferente a vacío.
        if okPressed and texto != '': 

            #? Si cant intems igual a cero.
            if cant_items == 0:
                self.opciones.insertItem(indice, texto) #* Agrega el texto en el indice que se está seleccionando.

                #? Si cant items es mayor o igual a cero.
            if cant_items >= 1:
                self.opciones.insertItem(indice, texto) #* Agrega el texto en el indice que se está seleccionando.
                self.opciones.setCurrentIndex(indice) #* Selecciona el último
            msg = QMessageBox(QMessageBox.Information, "Agregar item", "El item se ha agregado!") #! Crea popUp notificando agregado exitoso.
            msg.exec() #! Se ejecuta la notificación, esto devuelve el boton que se oprime.
    
        #? Si presiona Aceptar y texto es vacío.
        if okPressed and texto == '':
            msg = QMessageBox(QMessageBox.Warning, "Error", "El campo no puede estar vacío", QMessageBox.Yes) #! Crea popUp notificando agregado exitoso.
            msg.exec() #! Se ejecuta la notificación, esto devuelve el boton que se oprime.
            self.al_clic_agregar() #* Ejecuta nuevamente la función
#!------------------------------------------------------------------------------------------------------

    def al_clic_editar(self):
        indice = self.opciones.currentIndex() #* El indice del indice en el que estamos posicionados.
        texto, okPressed = QInputDialog.getText(self, "Editar item", "Ingresa nuevo nombre: ")

        if okPressed and texto != '':
            msg = QMessageBox(QMessageBox.Warning, "Editar item", "¿Seguro quieres editar el item?", QMessageBox. Yes | QMessageBox.No)
            resultado = msg.exec()
            if resultado == QMessageBox.Yes:
                self.opciones.removeItem(indice)
                self.opciones.addItem(texto)
                msg = QMessageBox(QMessageBox.Warning, "Editar item", "Item editado.")
            if resultado == QMessageBox.No:
                pass
        if texto == False:
            pass

        if okPressed and texto == '':
            msg = QMessageBox(QMessageBox.Critical, "Editar item", "El campo no puede estar vacío.")
            msg.exec()
            self.al_clic_editar()

#!------------------------------------------------------------------------------------------------------

    def al_clic_quitar(self):
        indice = self.opciones.currentIndex()
        msg = QMessageBox(QMessageBox.Warning, "Eliminar item", "¿Seguro quieres eliminar el item?",QMessageBox. Yes | QMessageBox.No)
        resultado = msg.exec()
        if resultado == QMessageBox.Yes:
            self.opciones.removeItem(indice)
            msg = QMessageBox(QMessageBox.Warning, "Eliminar item", "Item eliminado.", QMessageBox. Yes)
            msg.exec()
        else:
            pass

#!------------------------------------------------------------------------------------------------------
     
    def al_clic_quitar_todos(self):
        msg = QMessageBox(QMessageBox.Warning, "Eliminar item", "¿Seguro quieres eliminar todos los items?", QMessageBox. Yes | QMessageBox.No)
        resultado = msg.exec()
        if resultado == QMessageBox.Yes:
            self.opciones.clear()
            msg = QMessageBox(QMessageBox.Warning, "Eliminar item", "Eliminaste todos los items.", QMessageBox. Yes)
        else:
            pass
#!------------------------------------------------------------------------------------------------------

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()