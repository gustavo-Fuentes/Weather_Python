from app.view.user_interface_base import Ui_MainWindow
from PyQt5 import QtWidgets
from app.service.api_service import OpenWeatherMap

class UserInterface(Ui_MainWindow, QtWidgets.QMainWindow):
    
    
    def __init__(self):
        self.api = OpenWeatherMap()
        
        
        
        super(QtWidgets.QMainWindow, self).__init__() # roda os metodos do pai
        self.setupUi(self)
        self.connectButtons()
     
    
    def getCity(self):
        return self.lineEdit.text()
        #print( self.lineEdit.text())
    
    
    def connectButtons(self):
        self.btn_buscar.clicked.connect(self.setValueTable)
        
        
    def setValueTable(self):
        dictionary = self.api.getForecast(self.getCity())      
        
        for i,previsao in enumerate(dictionary["daily"]):
   
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem( str(previsao["temp"]["max"]) ))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem( str(previsao["temp"]["min"]) ))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem( str(previsao["humidity"]) ))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem( str(previsao.get("rain", "sem previsão")) ))