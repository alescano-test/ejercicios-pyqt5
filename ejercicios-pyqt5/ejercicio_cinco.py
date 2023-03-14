from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

'''
Realizar un programa que permita realizar una conversión de unidades de temperatura.
'''


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_cinco.ui", self)
        self.calcular.clicked.connect(self.calcular_temperatura)

    def calcular_temperatura(self):
        lenDato = len(self.input_temp.text())
        resultado = 0
        if lenDato == 0:
            msg = QMessageBox(QMessageBox.Warning, "Error",
                              "El valor es requerido.")
            msg.exec()
        if lenDato >= 1:
            if self.centigrados_kelvin.isChecked():
                resultado = f"(K°) {float(self.input_temp.text()) + 273.15}"
            if self.kelvin_centigrados.isChecked():
                resultado = f"(C°) {float(self.input_temp.text()) - 273.15}"
            if self.centigrados_fahrenheit.isChecked():
                resultado = f"(F°) {float(self.input_temp.text())  * 1.8 + 32}"
            if self.fahrenheit_centigrados.isChecked():
                resultado = f"(C°) {round(float(self.input_temp.text()),2) - 32 / 1.8}"

        self.conversion.setText(str(resultado))


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
