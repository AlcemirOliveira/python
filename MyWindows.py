from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Cash Flow"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.setWindowIcon(QtGui.QIcon('icone.jpg'))
        self.show()

App =  QApplication(sys.argv)
window = Window()
sys.exit(App.exec())



