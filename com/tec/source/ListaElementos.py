from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize, QRect, QCoreApplication
from PySide2.QtGui import QColor, QBrush, QIcon, Qt, QCursor
from PySide2.QtWidgets import QListWidgetItem
import source_rc

#Lista que contiene los elementos a añadir
class ListaElementos(QtWidgets.QListWidget):#lista que contiene los items para crear Elementos en la Table
    def __init__(self, parent=None):
        super(ListaElementos, self).__init__(parent)

        icon = QIcon()
        icon.addFile(u":/bback/addpower.png", QSize(), QIcon.Normal, QIcon.Off)
        brush4 = QBrush(QColor(222, 176, 6, 255))
        brush4.setStyle(Qt.NoBrush)
        __qlistwidgetitem = QListWidgetItem(self)
        __qlistwidgetitem.setForeground(brush4)
        __qlistwidgetitem.setIcon(icon)
        __qlistwidgetitem.setText("Fuente")

        icon1 = QIcon()
        icon1.addFile(u":/bback/addresistor.png", QSize(), QIcon.Normal, QIcon.Off)
        brush5 = QBrush(QColor(11, 173, 154, 255))
        brush5.setStyle(Qt.NoBrush)
        __qlistwidgetitem1 = QListWidgetItem(self)
        __qlistwidgetitem1.setForeground(brush5)
        __qlistwidgetitem1.setIcon(icon1)
        __qlistwidgetitem1.setText("Resistencia")

        self.setObjectName(u"listaElementos")
        self.setGeometry(QRect(940, 135, 201, 141))

        self.viewport().setProperty('cursor', QCursor(Qt.ClosedHandCursor))

        self.setStyleSheet(u"background-color: rgb(106,193,224);\n""font: 17pt \"OCR A Extended\";\n""border-radius: 10px;")

        self.setIconSize(QSize(40,40))

        self.setDragEnabled(True)


    def mousePressEvent(self,event):#al seleccionar un icono

        item = self.itemAt(event.pos())#encuentra el item en la posición


        name = item.text()#el texto que contenga el item

        drag = QtGui.QDrag(self)
        mime_data = QtCore.QMimeData()

        mime_data.setText(name)
        drag.setMimeData(mime_data)
        drag.exec_()

        super(ListaElementos, self).mousePressEvent(event)