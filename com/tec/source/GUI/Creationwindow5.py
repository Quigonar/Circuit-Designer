# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Creationwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1160, 830)
        Form.setStyleSheet(u"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 20, 421, 111))
        palette = QPalette()
        brush = QBrush(QColor(165, 132, 48, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(65, 113, 121, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label.setPalette(palette)
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(30)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.backbutton = QPushButton(Form)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(1090, 20, 51, 41))
        font1 = QFont()
        font1.setFamily(u"PT Bold Broken")
        font1.setPointSize(31)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.backbutton.setFont(font1)
        self.backbutton.setCursor(QCursor(Qt.ArrowCursor))
        self.backbutton.setStyleSheet(u"image: url(:/bback/back.png);\n"
"border-width: 2px;\n"
"	border-radius: 10px;")
        self.backbutton.setAutoDefault(False)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 1161, 831))
        self.label_6.setStyleSheet(u"image: url(:/bback/decoration.png);")
        self.simularButton = QPushButton(Form)
        self.simularButton.setObjectName(u"simularButton")
        self.simularButton.setGeometry(QRect(1030, 680, 121, 91))
        font2 = QFont()
        font2.setPointSize(16)
        self.simularButton.setFont(font2)
        self.simularButton.setStyleSheet(u"background-image: url(:/bback/simularbutton.png);\n"
"border-radius: 10px;")
        self.editor = QWidget(Form)
        self.editor.setObjectName(u"editor")
        self.editor.setGeometry(QRect(20, 130, 1021, 661))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(830, 80, 201, 51))
        font3 = QFont()
        font3.setFamily(u"OCR A Extended")
        font3.setPointSize(20)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgb(75, 87, 98);\n"
"border-radius: 10px;")
        self.label_6.raise_()
        self.label.raise_()
        self.backbutton.raise_()
        self.simularButton.raise_()
        self.editor.raise_()
        self.label_5.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CREADOR DE CIRCUITOS", None))
        self.backbutton.setText("")
        self.label_6.setText("")
        self.simularButton.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">ELEMENTOS</p></body></html>", None))
    # retranslateUi

