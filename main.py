import sys
from app.view.user_interface import UserInterface
from PyQt5 import QtWidgets


    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit( app.exec_() )