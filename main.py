from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6 import QtCore
from Articles import Ui_MainWindow 
from db import DatabaseHandler
from PySide6.QtCore import QDate

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

        self.ui.tableArticles.selectionModel().selectionChanged.connect(self.enable_buttons)
        self.ui.tableAuthors.selectionModel().selectionChanged.connect(self.enable_buttons)
        self.ui.tableJournals.selectionModel().selectionChanged.connect(self.enable_buttons)
        self.ui.tableTopics.selectionModel().selectionChanged.connect(self.enable_buttons)

        self.ui.tabWidget_2.currentChanged.connect(self.loadData)
        self.loadData()
        self.load_authors()
        self.load_journals()
        self.load_topics()

        #дата
        self.ui.dataArticles.setDate(QDate.currentDate())
        self.ui.dataJournal.setDate(QDate.currentDate())

        #Кнопки       
        self.ui.addTopic.clicked.connect(self.add_topics)
        self.ui.addJournal.clicked.connect(self.add_journals)
        self.ui.addAuthors.clicked.connect(self.add_author)
        self.ui.addArticles.clicked.connect(self.add_articles)

        self.ui.delAuthor.clicked.connect(self.del_record)
        self.ui.delJournals.clicked.connect(self.del_record)
        self.ui.delTopic.clicked.connect(self.del_record)
        self.ui.delArticles.clicked.connect(self.del_record)

        self.ui.findArticles.textChanged.connect(self.find_Value)
        self.ui.findAuthors.textChanged.connect(self.find_Value)
        self.ui.findArticles_2.textChanged.connect(self.find_Value)
        self.ui.findTopic.textChanged.connect(self.find_Value)

        self.ui.completeArticles.clicked.connect(self.update_articles)
        self.ui.completeJournal.clicked.connect(self.update_journals)
        self.ui.completeAuthors.clicked.connect(self.update_author)
        self.ui.completeTopic.clicked.connect(self.update_topic)

        self.ui.editJournals.clicked.connect(self.update)
        self.ui.editArticles.clicked.connect(self.update)
        self.ui.editAuthor.clicked.connect(self.update)
        self.ui.editTopic.clicked.connect(self.update)

    def loadData(self):
        current_text = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())

        if current_text == "Статьи":            
            items = self.db_handler.load_data(current_text)
            headers = self.db_handler.load_headers(current_text)
            self.atriclesModel.setItems(items)
            self.atriclesModel.setName(headers)
            self.ui.tableArticles.setColumnHidden(0, True) 

        if current_text == "Журналы":
            items = self.db_handler.load_data(current_text)
            headers = self.db_handler.load_headers(current_text)
            self.journalModel.setItems(items)
            self.journalModel.setName(headers)
            self.ui.tableJournals.setColumnHidden(0, True)

        if current_text == "Авторы":
            items = self.db_handler.load_data(current_text)
            headers = self.db_handler.load_headers(current_text)
            self.authorModel.setItems(items)
            self.authorModel.setName(headers)
            self.ui.tableAuthors.setColumnHidden(0, True)

        if current_text == "Темы": 
            items = self.db_handler.load_data(current_text)
            headers = self.db_handler.load_headers(current_text)
            self.topicModel.setItems(items)
            self.topicModel.setName(headers)
            self.ui.tableTopics.setColumnHidden(0, True)

    def currentElement(self):
        tableName = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())

        tables = {
        'Авторы': self.ui.tableAuthors,
        'Журналы': self.ui.tableJournals,
        'Темы': self.ui.tableTopics,
        'Статьи': self.ui.tableArticles}

        tablesmodel = {'Авторы': self.authorModel,
                  'Темы': self.topicModel,
                  'Журналы': self.journalModel,
                  'Статьи': self.atriclesModel}
        
        table = tables[tableName]
        model = tablesmodel[tableName]
        row = table.currentIndex()
        if not row.isValid():
            QMessageBox.warning(self, "Ошибка", "Не выбрана строка для редактирования")
            return
        cell_index = row.sibling(row.row(), 0)
        id = cell_index.data()

        return [id, tableName, table, model]
    
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
        self.ui.parentTopic.addItems(items)
    
    def enable_buttons(self):
        tableName = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())
        if tableName == "Статьи":
            if self.ui.tableArticles.currentIndex().isValid():
                self.ui.editArticles.setEnabled(True)
                self.ui.delArticles.setEnabled(True)
        if tableName == "Авторы":
            if self.ui.tableAuthors.currentIndex().isValid():
                self.ui.editAuthor.setEnabled(True)
                self.ui.delAuthor.setEnabled(True)

        if tableName == "Журналы":
            if self.ui.tableJournals.currentIndex().isValid():
                self.ui.editJournals.setEnabled(True)
                self.ui.delJournals.setEnabled(True)

        if tableName == "Темы":
            if self.ui.tableTopics.currentIndex().isValid():
                self.ui.editTopic.setEnabled(True)
                self.ui.delTopic.setEnabled(True)

    def disable_buttons(self):
        self.ui.editTopic.setEnabled(False)
        self.ui.delTopic.setEnabled(False)
        self.ui.editAuthor.setEnabled(False)
        self.ui.delAuthor.setEnabled(False)
        self.ui.editJournals.setEnabled(False)
        self.ui.delJournals.setEnabled(False)
        self.ui.editArticles.setEnabled(False)
        self.ui.delArticles.setEnabled(False)
    
    def clear_article(self):       
        self.ui.nameArticle.clear()
        self.ui.volume.clear()
        self.ui.pagesArticles.clear()
        self.ui.abstract_2.clear()
        self.ui.lineEdit.clear()

    def clear_journal(self):        
        self.ui.nameJournal.clear()
        self.ui.issnJournal.clear()
        self.ui.publisher.clear()
        self.ui.period.clear()

    def clear_topic(self):        
        self.ui.nameTopic.clear()
        self.ui.descriptionTopic.clear()

    def clear_author(self):        
        self.ui.FIO.clear()
        self.ui.affiliation.clear()
        self.ui.email.clear()

    def add_articles(self):
        tableName = "Статьи"
        self.disable_buttons()
        name = self.ui.nameArticle.text().strip()
        author = self.ui.articlesAuthor.currentText()
        journal = self.ui.ArticlesJournal.currentText()
        date = self.ui.dataArticles.text()
        volume = self.ui.volume.text().strip()
        theme = self.ui.topicArticles.currentText()
        pages = self.ui.pagesArticles.text()
        abstract = self.ui.abstract_2.toPlainText()
        link = self.ui.lineEdit.text().strip()
        if name and date and volume and pages and abstract and link:
            if len(name)<200 and len(volume)<20 and pages.isdigit():
                try:
                    self.db_handler.addRecord(tableName, (name, author, journal, date, volume, theme, pages, abstract, link))
                    self.clear_article()
                    self.loadData()
                    self.ui.articlesWarning.setText(" ")
                    self.ui.completeArticles.setEnabled(False)

                except Exception as e:
                    self.ui.articlesWarning.setText(f"Проверьте данные!\nНазвание должно быть меньше 200 симв(у вас: {len(name)});\nНазвание тома должно быть меньше 20 симв (у вас: {len(volume)});\nКоличество страниц должно быть числом")
                    self.ui.articlesWarning.setStyleSheet("color: red;")
            else:
                self.ui.articlesWarning.setText(f"Проверьте данные!\nНазвание должно быть меньше 200 симв(у вас: {len(name)});\nНазвание тома должно быть меньше 20 симв (у вас: {len(volume)});\nКоличество страниц должно быть числом")
                self.ui.articlesWarning.setStyleSheet("color: red;")
                return
        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")


    def add_journals(self):
        tableName = "Журналы"
        self.disable_buttons()
        name = self.ui.nameJournal.text().strip()        
        issn = self.ui.issnJournal.text().strip()
        publisher = self.ui.publisher.text().strip()
        data = self.ui.dataJournal.text().strip()
        period = self.ui.period.text().strip()
        if name and issn and publisher and data and period:
            if len(issn)==9 and len(period)<30:
                try:
                    self.db_handler.addRecord(tableName, (name, issn, publisher, data, period))
                    self.clear_journal()
                    self.loadData()
                    self.load_journals()
                    self.ui.completeJournal.setEnabled(False)
                    self.ui.addJournal.setEnabled(True)
                    self.ui.journalWarning.setText(" ")
                except Exception as e:
                    self.ui.journalWarning.setText(f"Проверьте данные!\nИндентификатор должен содержать 9 симв.(у вас: {len(issn)})\nПереодичность должна быть меньше 30 симв.(у вас: {len(period)})\nНазвание и идентификатор не должны повторяться")
                    self.ui.journalWarning.setStyleSheet("color: red;")
            else:
                self.ui.journalWarning.setText(f"Проверьте данные!\nИндентификатор должен содержать 9 симв.(у вас: {len(issn)})\nПереодичность должна быть меньше 30 симв.(у вас: {len(period)})\nНазвание и идентификатор не должны повторяться")
                self.ui.journalWarning.setStyleSheet("color: red;")
        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")


    def add_author(self):
        tableName = "Авторы"
        self.disable_buttons()
        full_name = self.ui.FIO.text().strip()        
        affiliationn = self.ui.affiliation.text().strip()
        emaill = self.ui.email.text().strip()
        if full_name and affiliationn and emaill:
            if len(affiliationn)<100 and len(emaill)<100:
                try:
                    self.db_handler.addRecord(tableName, (full_name, affiliationn, emaill))
                    self.clear_author()
                    self.loadData()
                    self.load_authors()
                    self.ui.completeAuthors.setEnabled(False)
                    self.ui.addAuthors.setEnabled(True)
                    self.ui.authorsWarning.setText(" ")
                except Exception as e:
                    self.ui.authorsWarning.setText(f"Проверьте данные!\nНазвание организации должно быть меньше 100 симв(у вас: {len(affiliationn)}\nПочта должна быть меньше 100 симв(у вас: {len(emaill)})\nИмя автора не должно повторяться")
                    self.ui.authorsWarning.setStyleSheet("color: red;")
            else:
                self.ui.authorsWarning.setText(f"Проверьте данные!\nНазвание организации должно быть меньше 100 симв(у вас: {len(affiliationn)}\nПочта должна быть меньше 100 симв(у вас: {len(emaill)})\nИмя автора не должно повторяться")
                self.ui.authorsWarning.setStyleSheet("color: red;")
        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")


    def add_topics(self):
        tableName = "Темы"
        self.disable_buttons()
        name = self.ui.nameTopic.text().strip()
        childeName = self.ui.parentTopic.currentText().strip()
        description = self.ui.descriptionTopic.toPlainText().strip()
        if name and description:
            if len(name)<100:
                if not childeName:
                    childeName = " "
                try:
                    self.db_handler.addRecord(tableName, (name, childeName, description))
                    self.clear_topic()
                    self.loadData()     
                    self.load_topics()       
                    self.ui.completeTopic.setEnabled(False)        
                except Exception as e:
                    self.ui.topicWarning.setText(f"Проверьте данные!\nНазвание темы должно быть меньше 100 симв(у вас: {len(name)})\nНазвание темы не должно повторяться")
                    self.ui.topicWarning.setStyleSheet("color: red;")
            else:
                self.ui.topicWarning.setText(f"Проверьте данные!\nНазвание темы должно быть меньше 100 симв(у вас: {len(name)})\nНазвание темы не должно повторяться")
                self.ui.topicWarning.setStyleSheet("color: red;")
        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")
        

    def del_record(self):
        tableName = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())
        table_mapping = {
        'Авторы': self.ui.tableAuthors,
        'Журналы': self.ui.tableJournals,
        'Темы': self.ui.tableTopics,
        'Статьи': self.ui.tableArticles}
        
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

    def find_Value(self, currentText):
        tableName = self.ui.tabWidget_2.tabText(self.ui.tabWidget_2.currentIndex())
        tablesmodel = {'Авторы': self.authorModel,
                  'Темы': self.topicModel,
                  'Журналы': self.journalModel,
                  'Статьи': self.atriclesModel}
        
        tables = {'Авторы': self.ui.tableAuthors,
                  'Темы': self.ui.tableTopics,
                  'Журналы': self.ui.tableJournals,
                  'Статьи': self.ui.tableArticles}
        
        if tableName not in tables:
            QMessageBox.warning(self, "Ошибка", "Неизвестный тип записи")
            return
        
        model = tablesmodel[tableName]
        table = tables[tableName]
        text = "%" + currentText + "%"

        if not currentText:
            self.loadData()

        try:            
            items = self.db_handler.findValue(tableName, text)
            headers = self.db_handler.load_headers(tableName)
            model.setItems(items)
            model.setName(headers)
            table.setColumnHidden(0, True)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"{e}")    
            
    def update(self):
        info = self.currentElement()
        self.disable_buttons()
        try:
            data = self.db_handler.findID(info[1], info[0])
            if info[1] == "Авторы":                
                self.ui.FIO.setText(data[0][1])        
                self.ui.affiliation.setText(data[0][2])
                self.ui.email.setText(data[0][3])
                self.ui.completeAuthors.setEnabled(True)
                self.ui.addAuthors.setEnabled(False)

            if info[1] == "Журналы":                
                self.ui.nameJournal.setText(data[0][1])
                self.ui.issnJournal.setText(data[0][2])
                self.ui.publisher.setText(data[0][3])
                self.ui.period.setText(data[0][5])
                self.ui.completeJournal.setEnabled(True)
                self.ui.addJournal.setEnabled(False)

            if info[1] == "Темы":
                self.ui.nameTopic.setText(data[0][1])
                self.ui.parentTopic.setCurrentText(data[0][2])
                self.ui.descriptionTopic.setText(data[0][3])
                self.ui.completeTopic.setEnabled(True)
                self.ui.addTopic.setEnabled(False)

            if info[1] == "Статьи":
                self.ui.nameArticle.setText(data[0][1])
                self.ui.articlesAuthor.setCurrentText(data[0][2])
                self.ui.ArticlesJournal.setCurrentText(data[0][3])
                self.ui.volume.setText(data[0][5])
                self.ui.topicArticles.setCurrentText(data[0][6])
                self.ui.pagesArticles.setText(str(data[0][7]))
                self.ui.abstract_2.setText(data[0][8])
                self.ui.lineEdit.setText(data[0][9])
                self.ui.addArticles.setEnabled(False)
                self.ui.completeArticles.setEnabled(True)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"{e}")

    def update_articles(self):
        info = self.currentElement()

        if info[1] == "Статьи":
            self.disable_buttons()
            name = self.ui.nameArticle.text().strip()
            author = self.ui.articlesAuthor.currentText()
            journal = self.ui.ArticlesJournal.currentText()
            date = self.ui.dataArticles.text()
            volume = self.ui.volume.text().strip()
            theme = self.ui.topicArticles.currentText()
            pages = self.ui.pagesArticles.text()
            abstract = self.ui.abstract_2.toPlainText()
            link = self.ui.lineEdit.text().strip()
            if name and date and volume and pages and abstract and link:
                if len(name)<200 and len(volume)<20 and pages.isdigit():                
                    try:
                        self.db_handler.updateValue(info[1], (name, author, journal, date, volume, theme, pages, abstract, link, info[0]))
                        self.clear_article()
                        self.loadData()
                        self.ui.completeArticles.setEnabled(False)
                        self.ui.addArticles.setEnabled(True)
                    except Exception as e:
                        self.ui.articlesWarning.setText(f"Проверьте данные!\nНазвание должно быть меньше 200 симв(у вас: {len(name)});\nНазвание тома должно быть меньше 20 симв (у вас: {len(volume)});\nКоличество страниц должно быть числом")
                        self.ui.articlesWarning.setStyleSheet("color: red;")
                else:
                    self.ui.articlesWarning.setText(f"Проверьте данные!\nНазвание должно быть меньше 200 симв(у вас: {len(name)});\nНазвание тома должно быть меньше 20 симв (у вас: {len(volume)});\nКоличество страниц должно быть числом")
                    self.ui.articlesWarning.setStyleSheet("color: red;")
            else:
                QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")

    def update_journals(self):
        info = self.currentElement()
        print(info[1])
        self.disable_buttons()
        name = self.ui.nameJournal.text().strip()        
        issn = self.ui.issnJournal.text().strip()
        publisher = self.ui.publisher.text().strip()
        data = self.ui.dataJournal.text().strip()
        period = self.ui.period.text().strip()
        if name and issn and publisher and data and period:
            if len(issn)==9 and len(period)<30:                
                try:
                    self.db_handler.updateValue(info[1], (name, issn, publisher, data, period, info[0]))
                    self.clear_journal()
                    self.loadData()
                    self.load_journals()
                    self.ui.completeJournal.setEnabled(False)
                    self.ui.addJournal.setEnabled(True)
                except Exception as e:
                    self.ui.journalWarning.setText(f"Проверьте данные!\nИндентификатор должен содержать 9 симв.(у вас: {len(issn)})\nПереодичность должна быть меньше 30 симв.(у вас: {len(period)})\nНазвание и идентификатор не должны повторяться{e}")
                    self.ui.journalWarning.setStyleSheet("color: red;")
            else:
                    self.ui.journalWarning.setText(f"Проверьте данные!\nИндентификатор должен содержать 9 симв.(у вас: {len(issn)})\nПереодичность должна быть меньше 30 симв.(у вас: {len(period)})\nНазвание и идентификатор не должны повторяться")
                    self.ui.journalWarning.setStyleSheet("color: red;")    
        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")

    def update_topic(self):
        info = self.currentElement()
        self.disable_buttons()
        name = self.ui.nameTopic.text().strip()
        childeName = self.ui.parentTopic.currentText().strip()
        description = self.ui.descriptionTopic.toPlainText().strip()
        if name and description:
            if len(name)<100:            
                if not childeName:
                    childeName = " "
                try:
                    self.db_handler.updateValue(info[1], (name, childeName, description, info[0]))
                    self.clear_topic()
                    self.loadData()     
                    self.load_topics()       
                    self.ui.completeTopic.setEnabled(False)
                    self.ui.addTopic.setEnabled(True)

                except Exception as e:
                    self.ui.topicWarning.setText(f"Проверьте данные!\nНазвание темы должно быть меньше 100 симв(у вас: {len(name)})\nНазвание темы не должно повторяться")
                    self.ui.topicWarning.setStyleSheet("color: red;")
            else:
                self.ui.topicWarning.setText(f"Проверьте данные!\nНазвание темы должно быть меньше 100 симв(у вас: {len(name)})\nНазвание темы не должно повторяться")
                self.ui.topicWarning.setStyleSheet("color: red;")
        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")

    def update_author(self):
        info = self.currentElement()
        self.disable_buttons()
        full_name = self.ui.FIO.text().strip()        
        affiliationn = self.ui.affiliation.text().strip()
        emaill = self.ui.email.text().strip()
        if full_name and affiliationn and emaill:
            if len(affiliationn)<100 and len(emaill)<100:
                try:
                    self.db_handler.updateValue(info[1], (full_name, affiliationn, emaill, info[0]))
                    self.clear_author()
                    self.loadData()
                    self.load_authors()
                    self.ui.completeAuthors.setEnabled(False)
                    self.ui.addAuthors.setEnabled(True)
                except Exception as e:
                    self.ui.authorsWarning.setText(f"Проверьте данные!\nНазвание организации должно быть меньше 100 симв(у вас: {len(affiliationn)}\nПочта должна быть меньше 100 симв(у вас: {len(emaill)})\nИмя автора не должно повторяться")
                    self.ui.authorsWarning.setStyleSheet("color: red;")
            else:
                self.ui.authorsWarning.setText(f"Проверьте данные!\nНазвание организации должно быть меньше 100 симв(у вас: {len(affiliationn)}\nПочта должна быть меньше 100 симв(у вас: {len(emaill)})\nИмя автора не должно повторяться")
                self.ui.authorsWarning.setStyleSheet("color: red;")
        else:
            QMessageBox.warning(self, "Ошибка", "Поля должны быть заполнены!")
 
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()