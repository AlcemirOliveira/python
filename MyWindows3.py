from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QToolTip,QMessageBox
from PyQt5.QtCore import QCoreApplication

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PERSONALIZANDO PUSHBUTTON"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        button = QPushButton("Sair",self)
        button.move(200,200)
        button.setStyleSheet('QPushButton {'
                             'background-color: red; '
                             'color: white; '
                             'font:bold 14px; '
                             'border-style:outset;'
                             'border-color:black;'
                             'border-width: 2px;'
                             'border-radius: 10px;}'
                             'QPushButton:pressed {background-color: yellow}')


        button.setToolTip('CLIQUE AQUI PARA SAIR')
        button.clicked.connect(self.CloseApp)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.setWindowIcon(QtGui.QIcon('icone.jpg'))
        self.show()

    def CloseApp(self):
        #QCoreApplication.instance().quit()
        reply=QMessageBox.question(self,'Sair do Programa','Deseja fechar o programa?',
                                   QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()



App =  QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())



