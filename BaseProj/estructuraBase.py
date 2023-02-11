from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

'''
'''
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("", self)
        

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()