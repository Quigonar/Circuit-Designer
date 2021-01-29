from PySide2 import QtWidgets,QtGui,QtCore
from PySide2.QtCore import QSize, QRect

from com.tec.source.GUI.Creationwindow5 import Ui_Form
from com.tec.source.Scene import EditScene
from com.tec.source.Table import Table
from com.tec.source.EventFilter import EventFilter
from com.tec.source.Elementos import Elementos
from com.tec.source.ListaElementos import ListaElementos
##
def Create_power():#Crea el nodo de la funete de poder
    nodo = Elementos()

    nodo.title = "Fuente de Poder"
    nodo.type_text = "Default"
    nodo.valor = 0

    nodo.add_conector(name="+",energy_o=True)
    nodo.add_conector(name="-")
    nodo.build()

    return nodo

def Create_resistor():#Crea el nodo de la resistencia
    nodo = Elementos()

    nodo.title = "Resistencia"
    nodo.type_text = "Default"
    nodo.valor = 0

    nodo.add_conector(name="<>")
    nodo.add_conector(name="<>")

    nodo.build()
    return nodo



class Createmode(QtWidgets.QWidget):#Crea la ventana y carga los elementos para poder editar el circuito
    def __init__(self):
        super(Createmode,self).__init__()

        #Cargando la Interfaz
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stack = QtWidgets.QStackedWidget()#Stack de lo widgets principales
        self.backb = self.ui.backbutton #boton para retroceder a la ventana main
        self.backb.clicked.connect(self.Back)

        self.scene = scene = EditScene()  # Crea la scene que guardará los gráficos
        self.contenedor = self.ui.editor #widget para insertar los gráficos
        self.simularB = self.ui.simularButton  # Boton para iniciar la simulación

        self.layout = QtWidgets.QHBoxLayout()

        self.listaElementos = ListaElementos(self)
        self.splitter = QtWidgets.QSplitter()

        self.layout.addWidget(self.splitter)
        self.contenedor.setLayout(self.layout)

        self.event_filter = EventFilter(self)


        self.scene.setSceneRect(0, 0, 999, 999)  # tamaño de la ascena
        self.view = Table(self.contenedor)
        self.view.setScene(self.scene)
        self.event_filter.install(self.scene)


        #Agregando elementos nuevos a la interfaz
        self.splitter.addWidget(self.view)
        self.splitter.addWidget(self.listaElementos)


        self.view.request_node.connect(self.Create_Elemento)

    def Back(self):#funcion para regresar a la primera pantalla
        self.stack.setCurrentIndex(0)
        self.scene.clear()#limpia la Table

    def setStack(self,stack):#obtiene el stack con las ventanas
        self.stack = stack

    def Create_Elemento(self,name):#Crea un nuevo elemento
        print("Creando nodo",name)
        if name == "Fuente":
            node = Create_power()
        elif name == "Resistencia":
            node = Create_resistor()

        self.scene.addItem(node)

        pos = self.view.mapFromGlobal(QtGui.QCursor.pos())#Obtiene la posición del mouse

        node.setPos(self.view.mapToScene(pos))#agrega el nodo en la posición de mouse





