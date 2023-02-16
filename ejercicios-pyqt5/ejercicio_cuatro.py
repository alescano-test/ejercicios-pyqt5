from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

'''
Realizar un programa que calcule el pedido de un lomito con los precios indicados
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_cuatro.ui", self)
        self.calcular.clicked.connect(self.calcularPrecio)

    def calcularPrecio(self):
        resultado = 0
        if self.carne.isChecked():
            resultado += 500
        if self.pollo.isChecked():
            resultado += 450
        if self.cerdo.isChecked():
            resultado += 400
        if self.huevo_frito.isChecked():
            resultado += 100
        if self.papas_fritas.isChecked():
            resultado += 200
        if self.gaseosa.isChecked():
            resultado += 250
        if self.delivery.isChecked():
            resultado += 100
        
        self.precio.setText(f"${resultado}")
    
app = QApplication([])
win = MiVentana()
win.show()
app.exec_()