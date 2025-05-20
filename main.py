from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Articles import Ui_MainWindow 
from db import init_db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    init_db()