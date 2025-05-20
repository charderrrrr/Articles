from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6 import QtCore
from Articles import Ui_MainWindow 
from db import DatabaseHandler
import sqlite3 as sl

items = [(1, 23, 4, 5), (3, 4, 5, 6), (6, 8, 56, 76)]
names = {0: "колонка 1", 1: "колонка 2", 2: "колонка 3", 3:"колонка 4"}

class tableModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = []
        self.headName = {}

    def setItems(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def setName(self, headName):
        self.beginResetModel()
        self.headName = headName
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)
    
    def columnCount(self, *args, **kwargs) -> int:
        if not self.items:
            return 0
        return len(self.items[0]) if self.items else 0
    
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return None
            
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()

            if row >= len(self.items) or col >= len(self.items[row]):
                return None
                
            return str(self.items[row][col])
            
        return None          


    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self.headName.get(section)
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_handler = DatabaseHandler()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        model = tableModel()
        model.setItems(items)
        model.setName(names)
        self.ui.tableArticles.setModel(model)
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()