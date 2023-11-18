from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QToolTip
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PERSONALIZANDO PUSHBUTTON"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        button = QPushButton("Salvar",self)
        button.move(200,200)
        button.setStyleSheet('QPushButton {'
                             'background-color: red; '
                             'color: white; '
                             'font:bold 14px; '
                             'border-style:outset;'
                             'border-color:black;'
                             'border-width: 2px;'
                             'border-radius: 10px;}')
        button.setToolTip('CLIQUE AQUI PARA SALVAR SEUS DADOS')

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.setWindowIcon(QtGui.QIcon('icone.jpg'))
        self.show()

App =  QApplication(sys.argv)
window = Window()
sys.exit(App.exec())



