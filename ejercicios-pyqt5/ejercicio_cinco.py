from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

'''
Realizar un programa que permita realizar una conversión de unidades de temperatura.
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/ejercicio_cinco.ui", self)
        self.calcular.clicked.connect(self.calcular_temperatura)

    
    def calcular_temperatura(self):
        resultado = 0
        if self.centigrados_kelvin.isChecked():
            resultado = f"(K°) {float(self.input_temp.text()) + 273.15}"
        if self.kelvin_centigrados.isChecked():
            resultado = f"(C°) {float(self.input_temp.text()) - 273.15}"
        if self.centigrados_fahrenheit.isChecked():
            resultado = f"(F°) {float(self.input_temp.text())  * 1.8 + 32}"
        if self.fahrenheit_centigrados.isChecked():
            resultado = f"(C°) {float(self.input_temp.text()) - 32 / 1.8}"
        
        self.conversion.setText(str(resultado))

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()