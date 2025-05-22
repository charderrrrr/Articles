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
        self.load_authors()
        self.load_journals()
        self.load_topics()

        #Кнопки       
        self.ui.addTopic.clicked.connect(self.add_topics)
        self.ui.addJournal.clicked.connect(self.add_journals)
        self.ui.addJournal_2.clicked.connect(self.add_author)
        self.ui.addArticles.clicked.connect(self.add_articles)

        self.ui.delArticles_2.clicked.connect(self.del_record)
        self.ui.delAuthors.clicked.connect(self.del_record)
        self.ui.delTopic.clicked.connect(self.del_record)

    def loadData(self):
        current_text = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())

        if current_text == "Статьи":            
            items = self.db_handler.load_data(f"articles")
            headers = self.db_handler.load_headers(f"articles")
            self.atriclesModel.setItems(items)
            self.atriclesModel.setName(headers)
            self.ui.tableArticles.setColumnHidden(0, True) 

        if current_text == "Журналы":
            items = self.db_handler.load_data(f"journals")
            headers = self.db_handler.load_headers(f"journals")
            self.journalModel.setItems(items)
            self.journalModel.setName(headers)
            self.ui.tableJournals.setColumnHidden(0, True)

        if current_text == "Авторы":
            items = self.db_handler.load_data(f"authors")
            headers = self.db_handler.load_headers(f"authors")
            self.authorModel.setItems(items)
            self.authorModel.setName(headers)
            self.ui.tableAuthors.setColumnHidden(0, True)

        if current_text == "Темы": 
            items = self.db_handler.load_data(f"topics")
            headers = self.db_handler.load_headers(f"topics")
            self.topicModel.setItems(items)
            self.topicModel.setName(headers)
            self.ui.tableTopics.setColumnHidden(0, True)

    def add_articles(self):
        tableName = "acticles"
        name = self.ui.nameArticle.text().strip()
        author = self.ui.articlesAuthor.currentText()
        journal = self.ui.ArticlesJournal.currentText()
        date = self.ui.dataArticles.text()
        volume = self.ui.volume.text().strip()
        theme = self.ui.topicArticles.currentText()
        pages = self.ui.pagesArticles.text()
        abstract = self.ui.abstract_2.toPlainText()
        link = self.ui.lineEdit.text().strip()
        if name and author and journal and date and volume and theme and pages and abstract and link:
            try:
                self.db_handler.addRecord(tableName, (name, author, journal, date, volume, theme, pages, abstract, link))
                self.ui.nameArticle.clear()
                self.ui.articlesAuthor.clear()
                self.ui.ArticlesJournal.clear()
                self.ui.dataArticles.clear()
                self.ui.volume.clear()
                self.ui.topicArticles.clear()
                self.ui.pagesArticles.clear()
                self.ui.abstract_2.clear()
                self.ui.lineEdit.clear()
                self.loadData()

            except Exception as e:
                print(f"Ошибка: {e}")


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
                self.load_journals()

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
                self.load_authors()
            except Exception as e:
                print(f"Ошибка: {e}")


    def add_topics(self):
        tableName = "topics"
        name = self.ui.nameTopic.text().strip()
        childeName = self.ui.childeTopic.text().strip()
        description = self.ui.descriptionTopic.toPlainText().strip()
        if name and childeName and description:
            if childeName:
                try:
                    self.db_handler.addRecord(tableName, (name, childeName, description))
                    self.ui.nameTopic.clear()
                    self.ui.childeTopic.clear()
                    self.ui.descriptionTopic.clear()
                    self.loadData()     
                    self.load_topics()               
                except Exception as e:
                    print(f"Ошибка: {e}")

        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")
        

    def del_record(self):
        tableName = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())
        table_mapping = {
        'Авторы': self.ui.tableAuthors,
        'Журналы': self.ui.tableJournals,
        'Темы': self.ui.tableTopics
            }
        if tableName not in table_mapping:
            QMessageBox.warning(self, "Ошибка", "Неизвестный тип записи")
            return
        
        table = table_mapping[tableName]
        row = table.currentIndex()
        if not row.isValid():
            QMessageBox.warning(self, "Ошибка", "Не выбрана строка для удаления")
            return
                
        cell_index = row.sibling(row.row(), 0)
        id = cell_index.data()

        reply = QMessageBox.question(self, "Подтверждение удаления", f"Вы действительно хотите удалить запись с ID {id}?",
        QMessageBox.Yes | QMessageBox.No)
    
        if reply == QMessageBox.No:
            return
        else:
            try:
                self.db_handler.delRecord(tableName, id)
                self.loadData()
                QMessageBox.information(self, "Успех", "Запись успешно удалена")
            except Exception as e:
                    QMessageBox.warning(self, "Ошибка", f"{e}")
      
    def load_authors(self):
        authors = self.db_handler.getAuthors()
        items = []
        for item in authors:
            items += item
        self.ui.articlesAuthor.addItems(items)
        
    def load_journals(self):
        journals = self.db_handler.getJournals()
        items = []
        for item in journals:
            items += item 
        self.ui.ArticlesJournal.addItems(items)

    def load_topics(self):
        topics = self.db_handler.getTopic()
        items = []
        for item in topics:
            items += item

        self.ui.topicArticles.addItems(items)
        


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()