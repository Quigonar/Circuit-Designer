from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize, QRect, QCoreApplication
from PySide2.QtGui import QColor, QBrush, QIcon, Qt, QCursor
from PySide2.QtWidgets import QListWidgetItem

class Listaresistencias(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(Listaresistencias, self).__init__(parent)

        self.setObjectName(u"listaresistencias")
        self.setGeometry(QRect(1030, 135, 141, 501))
        self.setStyleSheet(u"background-color: rgb(106,193,224);\n""font: 12pt \"OCR A Extended\";\n""border-radius: 10px;")
        self.brush = QBrush(QColor(23, 142, 166, 255))
        self.brush.setStyle(Qt.NoBrush)
        self.listaElementos = []
        self.last_selected = None

    def mousePressEvent(self, event):  # al seleccionar un icono
        item = self.itemAt(event.pos())  # encuentra el item en la posición
        if self.listaElementos:
            if self.last_selected:#elimina el estado de selección al elemento anterior
                self.last_selected.setSelected(False)
            for resitencia in self.listaElementos:
                if resitencia.type_text == item.text():
                    resitencia.setSelected(True)
                    self.last_selected = resitencia


        super(Listaresistencias, self).mousePressEvent(event)
    def Add_resistencia(self,name):#Añade el nombre de la resistencia a la lista
        qlistwidgetitem = QListWidgetItem(self)
        qlistwidgetitem.setForeground(self.brush)
        qlistwidgetitem.setText(name)

        self.addItem(qlistwidgetitem)
    def setListaElementos(self,lista):
        self.listaElementos = lista