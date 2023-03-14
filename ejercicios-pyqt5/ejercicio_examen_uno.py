from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

'''
'''


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_examen_uno.ui", self)
        self.calcular.clicked.connect(self.operaciones)

    def operaciones(self):
        resultado = 0
        msg = QMessageBox()

        if self.chSumar.isChecked() == True:
            resultado = float(self.inputA.text()) + float(self.inputB.text())
            msg = QMessageBox(QMessageBox.Information, "Resultado",
                              "El resultado de la suma es " + str(resultado))
            msg.exec()

        if self.chRestar.isChecked() == True:
            resultado = float(self.inputA.text()) - float(self.inputB.text())
            msg = QMessageBox(QMessageBox.Information, "Resultado",
                              "El resultado de la resta es " + str(resultado))
            msg.exec()

        if self.chMultiplicar.isChecked() == True:
            resultado = float(self.inputA.text()) * float(self.inputB.text())
            msg = QMessageBox(QMessageBox.Information, "Resultado",
                              "El resultado de la multiplicación es " + str(resultado))
            msg.exec()

        if self.chDividir.isChecked() == True:
            resultado = float(self.inputA.text()) / float(self.inputB.text())
            msg = QMessageBox(QMessageBox.Information, "Resultado",
                              "El resultado de la división es " + str(resultado))
            msg.exec()

        if self.chParImpar.isChecked() == True:
            if int(self.inputA.text()) % 2 == 0 and int(self.inputB.text()) % 2 == 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "A y B son pares ")
                msg.exec()
            if int(self.inputA.text()) % 2 == 1 and int(self.inputB.text()) % 2 == 1:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "A y B son impares")
                msg.exec()
            if int(self.inputA.text()) % 2 == 0 and int(self.inputB.text()) % 2 == 1:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "A es par y B es impar")
                msg.exec()
            if int(self.inputA.text()) % 2 == 1 and int(self.inputB.text()) % 2 == 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "A es impar y B es par")
                msg.exec()

        if self.chPosCerNeg.isChecked() == True:
            if float(self.inputA.text()) > 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "A es positivo")
                msg.exec()
            if float(self.inputA.text()) == 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "A es cero")
                msg.exec()
            if float(self.inputA.text()) < 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "A es negativo")
                msg.exec()
            if float(self.inputB.text()) > 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "B es positivo")
                msg.exec()
            if float(self.inputB.text()) == 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "B es cero")
                msg.exec()
            if float(self.inputB.text()) < 0:
                msg = QMessageBox(QMessageBox.Information,
                                  "Resultado", "B es negativo")
                msg.exec()

        if self.chSumar.isChecked() == False and self.chRestar.isChecked() == False and self.chMultiplicar.isChecked() == False and self.chDividir.isChecked() == False and self.chParImpar.isChecked() == False and self.chPosCerNeg.isChecked() == False:
            msg = QMessageBox(QMessageBox.Warning, "Error",
                              "No se seleccionó opción.")
            msg.exec()


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
