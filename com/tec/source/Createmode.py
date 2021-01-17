from PySide2 import QtWidgets

from com.tec.source.GUI.Creationwindow5 import Ui_Form
from com.tec.source.Scene import Scene
from com.tec.source.Table import Table
from com.tec.source.EventFilter import eventFilter

class Createmode(QtWidgets.QWidget):#Crea la ventana y carga los elementos para poder editar el circuito
    def __init__(self):
        super(Createmode,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stack = QtWidgets.QStackedWidget()
        self.backb = self.ui.backbutton
        self.backb.clicked.connect(self.Back)
        self.contenedor = self.ui.editor

        self.simularB = self.ui.simularButton#Boton para iniciar la simulación
        self.agregarResistencia = self.ui.resistenciaButton#boton que agrega la reistencia
        self.agregarPoder = self.ui.poderButton#boton que agrega la fuente de poder

        self.event_filter = eventFilter(self)

        self.scene = Scene()
        self.scene.setSceneRect(0,0,999,999)
        self.view = Table(self.contenedor)

        self.view.setScene(self.scene)
        self.event_filter.install(self.scene)


       # self.view.request_node.connect(self.create_node)
        # self.contenedor = Contenedor(self)

    def Back(self):#funcion para regresar a la primera pantalla
        self.stack.setCurrentIndex(0)

    def setStack(self,stack):#obtiene el stack con las ventanas
        self.stack = stack




