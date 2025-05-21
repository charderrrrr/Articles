from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6 import QtCore
from Articles import Ui_MainWindow 
from db import DatabaseHandler
import sqlite3 as sl

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
        
        #Модели
        self.atriclesModel = tableModel()
        self.ui.tableArticles.setModel(self.atriclesModel)
        self.topicModel = tableModel()
        self.ui.tableTopics.setModel(self.topicModel)
        self.authorModel = tableModel()
        self.ui.tableAuthors.setModel(self.authorModel)
        self.journalModel = tableModel()
        self.ui.tableJournals.setModel(self.journalModel)
        self.ui.tabWidget_2.currentChanged.connect(self.loadData)
        self.loadData()

        #Кнопки       
        self.ui.addTopic.clicked.connect(self.add_topics)
        self.ui.addJournal.clicked.connect(self.add_journals)
        self.ui.addJournal_2.clicked.connect(self.add_author)
        # self.ui.delAuthors.clicked.connect(self.del_author)


    def loadData(self):
        current_text = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())

        if current_text == "Статьи":            
            items = self.db_handler.load_data(f"articles")
            headers = self.db_handler.load_headers(f"articles")
            self.atriclesModel.setItems(items)
            self.atriclesModel.setName(headers)

        if current_text == "Журналы":
            items = self.db_handler.load_data(f"journals")
            headers = self.db_handler.load_headers(f"journals")
            self.journalModel.setItems(items)
            self.journalModel.setName(headers)

        if current_text == "Авторы":
            items = self.db_handler.load_data(f"authors")
            headers = self.db_handler.load_headers(f"authors")
            self.authorModel.setItems(items)
            self.authorModel.setName(headers)

        if current_text == "Темы": 
            items = self.db_handler.load_data(f"topics")
            headers = self.db_handler.load_headers(f"topics")
            self.topicModel.setItems(items)
            self.topicModel.setName(headers)

    
    def add_journals(self):
        tableName = "journals"
        name = self.ui.nameJournal.text().strip()        
        issn = self.ui.issnJournal.text().strip()
        publisher = self.ui.publisher.text().strip()
        data = self.ui.dataJournal.text().strip()
        period = self.ui.period.text().strip()
        if name and issn and publisher and data and period:
            try:
                self.db_handler.addRecord(tableName, (name, issn, publisher, data, period))
                self.ui.nameJournal.clear()
                self.ui.issnJournal.clear()
                self.ui.publisher.clear()
                self.ui.dataJournal.clear()
                self.ui.period.clear()
                self.loadData()

            except Exception as e:
                print(f"Ошибка: {e}")


    def add_author(self):
        tableName = "authors"
        full_name = self.ui.FIO.text().strip()        
        affiliationn = self.ui.affiliation.text().strip()
        emaill = self.ui.email.text().strip()
        if full_name and affiliationn and emaill:
            try:
                self.db_handler.addRecord(tableName, (full_name, affiliationn, emaill))
                self.ui.FIO.clear()
                self.ui.affiliation.clear()
                self.ui.email.clear()
                self.loadData()
            except Exception as e:
                print(f"Ошибка: {e}")


    def add_topics(self):
        tableName = "topics"
        name = self.ui.nameTopic.text().strip()
        childeName = self.ui.childeTopic.text().strip()
        description = self.ui.descriptionTopic.toPlainText().strip()
        if name and childeName and description:
            if int(childeName):
                try:
                    self.db_handler.addRecord(tableName, (name, childeName, description))
                    self.ui.nameTopic.clear()
                    self.ui.childeTopic.clear()
                    self.ui.descriptionTopic.clear()
                    self.loadData()
                except Exception as e:
                    print(f"Ошибка: {e}")

        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")
        
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()