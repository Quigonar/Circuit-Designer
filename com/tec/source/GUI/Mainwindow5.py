# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 908)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(40, 440, 241, 91))
        font = QFont()
        font.setFamily(u"STCaiyun")
        font.setPointSize(25)
        self.loadButton.setFont(font)
        self.loadButton.setStyleSheet(u"background-color: rgb(162, 162, 162);\n"
"border-radius: 30px;")
        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(40, 550, 241, 91))
        self.createButton.setFont(font)
        self.createButton.setStyleSheet(u"background-color: rgb(133, 161, 161);\n"
"border-radius: 30px;l")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 30, 721, 161))
        font1 = QFont()
        font1.setFamily(u"OCR A Extended")
        font1.setPointSize(50)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, -30, 1151, 951))
        self.label_2.setStyleSheet(u"image: url(:/bback/iprincipal.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.loadButton.raise_()
        self.createButton.raise_()
        self.label.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"CARGAR", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"CREAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CIRCUIT BUILDER", None))
        self.label_2.setText("")
    # retranslateUi

