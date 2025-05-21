# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Articles.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QTabWidget, QTableView, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1004, 766)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 591, 701))
        self.tabWidget_2 = QTabWidget(self.groupBox)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(20, 30, 551, 651))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.splitter_2 = QSplitter(self.tab_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(10, 520, 521, 47))
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.findArticles = QLineEdit(self.splitter)
        self.findArticles.setObjectName(u"findArticles")
        self.splitter.addWidget(self.findArticles)
        self.splitter_2.addWidget(self.splitter)
        self.comboBoxArticles = QComboBox(self.splitter_2)
        self.comboBoxArticles.addItem("")
        self.comboBoxArticles.addItem("")
        self.comboBoxArticles.addItem("")
        self.comboBoxArticles.addItem("")
        self.comboBoxArticles.addItem("")
        self.comboBoxArticles.addItem("")
        self.comboBoxArticles.addItem("")
        self.comboBoxArticles.setObjectName(u"comboBoxArticles")
        self.splitter_2.addWidget(self.comboBoxArticles)
        self.delArticles = QPushButton(self.tab_4)
        self.delArticles.setObjectName(u"delArticles")
        self.delArticles.setGeometry(QRect(410, 580, 121, 31))
        self.editArticles = QPushButton(self.tab_4)
        self.editArticles.setObjectName(u"editArticles")
        self.editArticles.setGeometry(QRect(270, 580, 131, 31))
        self.tableArticles = QTableView(self.tab_4)
        self.tableArticles.setObjectName(u"tableArticles")
        self.tableArticles.setGeometry(QRect(10, 20, 521, 481))
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.delAuthors = QPushButton(self.tab_5)
        self.delAuthors.setObjectName(u"delAuthors")
        self.delAuthors.setGeometry(QRect(410, 580, 121, 31))
        self.splitter_10 = QSplitter(self.tab_5)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setGeometry(QRect(10, 520, 521, 47))
        self.splitter_10.setOrientation(Qt.Orientation.Vertical)
        self.splitter_11 = QSplitter(self.splitter_10)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setOrientation(Qt.Orientation.Horizontal)
        self.label_9 = QLabel(self.splitter_11)
        self.label_9.setObjectName(u"label_9")
        self.splitter_11.addWidget(self.label_9)
        self.findAuthors = QLineEdit(self.splitter_11)
        self.findAuthors.setObjectName(u"findAuthors")
        self.splitter_11.addWidget(self.findAuthors)
        self.splitter_10.addWidget(self.splitter_11)
        self.comboBoxAuthors = QComboBox(self.splitter_10)
        self.comboBoxAuthors.addItem("")
        self.comboBoxAuthors.addItem("")
        self.comboBoxAuthors.addItem("")
        self.comboBoxAuthors.setObjectName(u"comboBoxAuthors")
        self.splitter_10.addWidget(self.comboBoxAuthors)
        self.editAuthors = QPushButton(self.tab_5)
        self.editAuthors.setObjectName(u"editAuthors")
        self.editAuthors.setGeometry(QRect(270, 580, 131, 31))
        self.tableJournals = QTableView(self.tab_5)
        self.tableJournals.setObjectName(u"tableJournals")
        self.tableJournals.setGeometry(QRect(10, 20, 521, 481))
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.delArticles_2 = QPushButton(self.tab_7)
        self.delArticles_2.setObjectName(u"delArticles_2")
        self.delArticles_2.setGeometry(QRect(410, 580, 121, 31))
        self.editArticles_2 = QPushButton(self.tab_7)
        self.editArticles_2.setObjectName(u"editArticles_2")
        self.editArticles_2.setGeometry(QRect(270, 580, 131, 31))
        self.splitter_3 = QSplitter(self.tab_7)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(10, 520, 521, 47))
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.splitter_4 = QSplitter(self.splitter_3)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Horizontal)
        self.label_17 = QLabel(self.splitter_4)
        self.label_17.setObjectName(u"label_17")
        self.splitter_4.addWidget(self.label_17)
        self.findArticles_2 = QLineEdit(self.splitter_4)
        self.findArticles_2.setObjectName(u"findArticles_2")
        self.splitter_4.addWidget(self.findArticles_2)
        self.splitter_3.addWidget(self.splitter_4)
        self.comboBoxArticles_2 = QComboBox(self.splitter_3)
        self.comboBoxArticles_2.addItem("")
        self.comboBoxArticles_2.addItem("")
        self.comboBoxArticles_2.addItem("")
        self.comboBoxArticles_2.addItem("")
        self.comboBoxArticles_2.setObjectName(u"comboBoxArticles_2")
        self.splitter_3.addWidget(self.comboBoxArticles_2)
        self.tableAuthors = QTableView(self.tab_7)
        self.tableAuthors.setObjectName(u"tableAuthors")
        self.tableAuthors.setGeometry(QRect(10, 20, 521, 481))
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.editTopic = QPushButton(self.tab_6)
        self.editTopic.setObjectName(u"editTopic")
        self.editTopic.setGeometry(QRect(270, 580, 131, 31))
        self.splitter_12 = QSplitter(self.tab_6)
        self.splitter_12.setObjectName(u"splitter_12")
        self.splitter_12.setGeometry(QRect(10, 520, 521, 47))
        self.splitter_12.setOrientation(Qt.Orientation.Vertical)
        self.splitter_14 = QSplitter(self.splitter_12)
        self.splitter_14.setObjectName(u"splitter_14")
        self.splitter_14.setOrientation(Qt.Orientation.Horizontal)
        self.label_11 = QLabel(self.splitter_14)
        self.label_11.setObjectName(u"label_11")
        self.splitter_14.addWidget(self.label_11)
        self.findTopic = QLineEdit(self.splitter_14)
        self.findTopic.setObjectName(u"findTopic")
        self.splitter_14.addWidget(self.findTopic)
        self.splitter_12.addWidget(self.splitter_14)
        self.comboBoxTopic = QComboBox(self.splitter_12)
        self.comboBoxTopic.addItem("")
        self.comboBoxTopic.addItem("")
        self.comboBoxTopic.addItem("")
        self.comboBoxTopic.setObjectName(u"comboBoxTopic")
        self.splitter_12.addWidget(self.comboBoxTopic)
        self.delTopic = QPushButton(self.tab_6)
        self.delTopic.setObjectName(u"delTopic")
        self.delTopic.setGeometry(QRect(410, 580, 121, 31))
        self.tableTopics = QTableView(self.tab_6)
        self.tableTopics.setObjectName(u"tableTopics")
        self.tableTopics.setGeometry(QRect(10, 20, 521, 481))
        self.tabWidget_2.addTab(self.tab_6, "")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(610, 10, 381, 701))
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 29, 361, 651))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.addArticles = QPushButton(self.tab)
        self.addArticles.setObjectName(u"addArticles")
        self.addArticles.setGeometry(QRect(10, 370, 341, 31))
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 361, 339))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.topicArticles = QComboBox(self.layoutWidget)
        self.topicArticles.setObjectName(u"topicArticles")

        self.gridLayout_3.addWidget(self.topicArticles, 5, 2, 1, 3)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 2)

        self.volume = QLineEdit(self.layoutWidget)
        self.volume.setObjectName(u"volume")

        self.gridLayout_3.addWidget(self.volume, 4, 2, 1, 3)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 2)

        self.articlesAuthor = QComboBox(self.layoutWidget)
        self.articlesAuthor.setObjectName(u"articlesAuthor")

        self.gridLayout_3.addWidget(self.articlesAuthor, 1, 2, 1, 3)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 2)

        self.pagesArticles = QLineEdit(self.layoutWidget)
        self.pagesArticles.setObjectName(u"pagesArticles")

        self.gridLayout_3.addWidget(self.pagesArticles, 6, 2, 1, 3)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)

        self.dataArticles = QDateEdit(self.layoutWidget)
        self.dataArticles.setObjectName(u"dataArticles")
        self.dataArticles.setMaximumDateTime(QDateTime(QDate(9999, 12, 28), QTime(16, 59, 59)))
        self.dataArticles.setDate(QDate(2025, 6, 17))

        self.gridLayout_3.addWidget(self.dataArticles, 3, 2, 1, 3)

        self.ArticlesJournal = QComboBox(self.layoutWidget)
        self.ArticlesJournal.setObjectName(u"ArticlesJournal")

        self.gridLayout_3.addWidget(self.ArticlesJournal, 2, 2, 1, 3)

        self.abstract_2 = QTextEdit(self.layoutWidget)
        self.abstract_2.setObjectName(u"abstract_2")

        self.gridLayout_3.addWidget(self.abstract_2, 7, 2, 1, 3)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 2)

        self.nameArticle = QLineEdit(self.layoutWidget)
        self.nameArticle.setObjectName(u"nameArticle")

        self.gridLayout_3.addWidget(self.nameArticle, 0, 2, 1, 3)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 8, 2, 1, 3)

        self.label_24 = QLabel(self.layoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 8, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.addJournal = QPushButton(self.tab_2)
        self.addJournal.setObjectName(u"addJournal")
        self.addJournal.setGeometry(QRect(10, 220, 341, 31))
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 361, 191))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.nameJournal = QLineEdit(self.layoutWidget1)
        self.nameJournal.setObjectName(u"nameJournal")

        self.gridLayout_2.addWidget(self.nameJournal, 0, 1, 1, 4)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.issnJournal = QLineEdit(self.layoutWidget1)
        self.issnJournal.setObjectName(u"issnJournal")

        self.gridLayout_2.addWidget(self.issnJournal, 1, 1, 1, 4)

        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)

        self.publisher = QLineEdit(self.layoutWidget1)
        self.publisher.setObjectName(u"publisher")

        self.gridLayout_2.addWidget(self.publisher, 2, 1, 1, 4)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)

        self.dataJournal = QDateEdit(self.layoutWidget1)
        self.dataJournal.setObjectName(u"dataJournal")
        self.dataJournal.setMaximumDateTime(QDateTime(QDate(9999, 12, 28), QTime(11, 59, 59)))
        self.dataJournal.setDate(QDate(2025, 6, 17))

        self.gridLayout_2.addWidget(self.dataJournal, 3, 1, 1, 4)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)

        self.period = QLineEdit(self.layoutWidget1)
        self.period.setObjectName(u"period")

        self.gridLayout_2.addWidget(self.period, 4, 1, 1, 4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.addJournal_2 = QPushButton(self.tab_8)
        self.addJournal_2.setObjectName(u"addJournal_2")
        self.addJournal_2.setGeometry(QRect(10, 140, 341, 31))
        self.layoutWidget2 = QWidget(self.tab_8)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 351, 111))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_21 = QLabel(self.layoutWidget2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.layoutWidget2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 3, 0, 1, 1)

        self.label_20 = QLabel(self.layoutWidget2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 0, 0, 1, 1)

        self.email = QLineEdit(self.layoutWidget2)
        self.email.setObjectName(u"email")

        self.gridLayout_4.addWidget(self.email, 3, 1, 1, 1)

        self.affiliation = QLineEdit(self.layoutWidget2)
        self.affiliation.setObjectName(u"affiliation")

        self.gridLayout_4.addWidget(self.affiliation, 1, 1, 1, 1)

        self.FIO = QLineEdit(self.layoutWidget2)
        self.FIO.setObjectName(u"FIO")

        self.gridLayout_4.addWidget(self.FIO, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.addTopic = QPushButton(self.tab_3)
        self.addTopic.setObjectName(u"addTopic")
        self.addTopic.setGeometry(QRect(10, 180, 341, 31))
        self.layoutWidget3 = QWidget(self.tab_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 10, 351, 151))
        self.gridLayout = QGridLayout(self.layoutWidget3)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.label_19 = QLabel(self.layoutWidget3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 2, 0, 1, 2)

        self.childeTopic = QLineEdit(self.layoutWidget3)
        self.childeTopic.setObjectName(u"childeTopic")

        self.gridLayout.addWidget(self.childeTopic, 1, 2, 1, 1)

        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMidLineWidth(0)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_18 = QLabel(self.layoutWidget3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 2)

        self.nameTopic = QLineEdit(self.layoutWidget3)
        self.nameTopic.setObjectName(u"nameTopic")

        self.gridLayout.addWidget(self.nameTopic, 0, 2, 1, 1)

        self.descriptionTopic = QTextEdit(self.layoutWidget3)
        self.descriptionTopic.setObjectName(u"descriptionTopic")

        self.gridLayout.addWidget(self.descriptionTopic, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1004, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBoxArticles.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043d\u0435\u0442", None))
        self.comboBoxArticles.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u0441\u0442\u0430\u0442\u044c\u0438", None))
        self.comboBoxArticles.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0436\u0443\u0440\u043d\u0430\u043b\u0443", None))
        self.comboBoxArticles.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0434\u0430\u0442\u0435", None))
        self.comboBoxArticles.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0442\u043e\u043c\u0443", None))
        self.comboBoxArticles.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0442\u0435\u043c\u0435", None))
        self.comboBoxArticles.setItemText(6, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043e\u0433\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u044e", None))

        self.delArticles.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.editArticles.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u044c\u0438", None))
        self.delAuthors.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBoxAuthors.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043d\u0435\u0442", None))
        self.comboBoxAuthors.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0430\u0432\u0442\u043e\u0440\u0443", None))
        self.comboBoxAuthors.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0441\u0444\u0435\u0440\u0435", None))

        self.editAuthors.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b\u044b", None))
        self.delArticles_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.editArticles_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBoxArticles_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043d\u0435\u0442", None))
        self.comboBoxArticles_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0438\u043c\u0435\u043d\u0438", None))
        self.comboBoxArticles_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.comboBoxArticles_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u043e email", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u044b", None))
        self.editTopic.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBoxTopic.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043d\u0435\u0442", None))
        self.comboBoxTopic.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.comboBoxTopic.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044e", None))

        self.delTopic.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u044b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.addArticles.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0430\u0442\u044c\u044e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0433\u043b\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"* \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u044c\u044f", None))
        self.addJournal.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0436\u0443\u0440\u043d\u0430\u043b", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"* \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434\u0438\u0447\u043d\u043e\u0441\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
        self.addJournal_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0432\u0442\u043e\u0440\u0430", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u044b", None))
        self.addTopic.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0435\u043c\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
    # retranslateUi

