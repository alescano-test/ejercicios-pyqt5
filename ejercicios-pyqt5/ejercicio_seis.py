from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

'''
Realizar un programa que permita generar un
dialogo de mensaje especificando el titulo, mensaje, icono y botones.
'''

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicios-pyqt5/interfaces/ejercicio_seis.ui", self)
        self.mostrar_mensaje.clicked.connect(self.mostrarMensaje)

    def mostrarMensaje(self):
        botones = 0
        mensaje = QMessageBox()
        mensaje.setWindowTitle(self.titulo_ventana.text())
        mensaje.setText(self.mensaje.text())
        if self.btn_ninguno.isChecked():
            mensaje
        if self.btn_informacion.isChecked():
            mensaje.setIcon(QMessageBox.Information)
        if self.btn_pregunta.isChecked():
            mensaje.setIcon(QMessageBox.Question)
        if self.btn_precaucion.isChecked():
            mensaje.setIcon(QMessageBox.Warning)
        if self.btn_critico.isChecked():
            mensaje.setIcon(QMessageBox.Critical)
        
        if self.ch_si.isChecked() == True:
            botones = botones | QMessageBox.Yes
        if self.ch_abrir.isChecked() == True:
            botones = botones | QMessageBox.Open
        if self.ch_abortar.isChecked() == True:
            botones = botones | QMessageBox.Abort
        if self.ch_no.isChecked() == True:
            botones = botones | QMessageBox.No
        if self.ch_cerrar.isChecked() == True:
            botones = botones | QMessageBox.Close
        if self.ch_reintentar.isChecked() == True:
            botones = botones | QMessageBox.Retry
        if self.ch_cancelar.isChecked() == True:
            botones = botones | QMessageBox.Cancel
        if self.ch_guardar.isChecked() == True:
            botones = botones | QMessageBox.Save
        if self.ch_ignorar.isChecked() == True:
            botones = botones | QMessageBox.Ignore
        if self.ch_ok.isChecked() == True:
            botones = botones | QMessageBox.Ok
        if self.ch_guardar_todo.isChecked() == True:
            botones = botones | QMessageBox.SaveAll
        
        mensaje.setStandardButtons(botones)
        mensaje.exec()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()