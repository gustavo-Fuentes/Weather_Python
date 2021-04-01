from app.view.user_interface_base import UIBase
from PyQt5 import QtWidgets

class UserInterface(UIBase, QtWidgets.QMainWindow):
    
    
    
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__() # roda os metodos do pai
        self.setupUi(self)
        self.connectButtons()
    
    
    def getCity(self):
        return self.lineEdit.text()
        #print( self.lineEdit.text())
    
    
    def connectButtons(self):
        self.btn_buscar.clicked.connect(self.getCity)