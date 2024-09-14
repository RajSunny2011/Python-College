# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.14
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.adminBooksFrame = QFrame(self.centralwidget)
        self.adminBooksFrame.setObjectName(u"adminBooksFrame")
        self.adminBooksFrame.setGeometry(QRect(0, 0, 801, 571))
        self.adminBooksFrame.setFrameShape(QFrame.StyledPanel)
        self.adminBooksFrame.setFrameShadow(QFrame.Raised)
        self.tableView = QTableView(self.adminBooksFrame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(-20, 0, 801, 491))
        self.searchBar = QLineEdit(self.adminBooksFrame)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(0, 0, 661, 28))
        self.searchBar.setFont(font)
        self.editButton = QPushButton(self.adminBooksFrame)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(100, 490, 91, 29))
        self.addButton = QPushButton(self.adminBooksFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(0, 490, 91, 29))
        self.addButton.setFont(font)
        self.searchButton = QPushButton(self.adminBooksFrame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(670, 0, 91, 29))
        self.deleteButton = QPushButton(self.adminBooksFrame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(200, 490, 91, 29))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuBooks = QMenu(self.menubar)
        self.menuBooks.setObjectName(u"menuBooks")
        self.menuUser = QMenu(self.menubar)
        self.menuUser.setObjectName(u"menuUser")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuBooks.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchBar.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit Entry", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add Entry", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Entry", None))
        self.menuBooks.setTitle(QCoreApplication.translate("MainWindow", u"Books", None))
        self.menuUser.setTitle(QCoreApplication.translate("MainWindow", u"User", None))
    # retranslateUi

