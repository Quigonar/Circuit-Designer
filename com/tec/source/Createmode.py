from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget

from com.tec.source.GUI.Creationwindow5 import Ui_Form


class Createmode(QtWidgets.QWidget):
    def __init__(self):
        super(Createmode,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stack = QtWidgets.QStackedWidget()
        self.backb = self.ui.backbutton
        self.backb.clicked.connect(self.Back)

        simularB = self.ui.simularButton#Boton para iniciar la simulación
        agregarResistencia = self.ui.resistenciaButton#boton que agrega la reistencia
        agregarPoder = self.ui.poderButton#boton que agrega la fuente de poder

    def Back(self):#funcion para regresar a la primera pantalla
        self.stack.setCurrentIndex(self.stack.currentIndex() - 1)

    def setStack(self,stack):#obtiene el stack con las ventanas
        self.stack = stack


