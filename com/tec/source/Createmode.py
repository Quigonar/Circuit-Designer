from PySide2 import QtWidgets,QtGui,QtCore
from PySide2.QtCore import QSize, QRect
from PySide2.QtGui import QFont

from com.tec.source.GUI.Creationwindow5 import Ui_Form
from com.tec.source.Scene import EditScene
from com.tec.source.Table import Table
from com.tec.source.EventFilter import EventFilter
from com.tec.source.Elementos import Elementos
from com.tec.source.ListaElementos import ListaElementos
from com.tec.source.Decoracion import *
from com.tec.source.ListaResistencias import Listaresistencias
##
lista_elementos = []


def Create_power():#Crea el nodo de la funete de poder
    nodo = Elementos()

    nodo.title = "Fuente de Poder"
    nodo.type_text = "Default"
    nodo.valor = 0
    nodo.setColor(QtGui.QColor(108, 191, 105,80))

    nodo.add_conector(name="+",energy_o=True)
    nodo.add_conector(name="-")
    nodo.build()

    lista_elementos.append(nodo)
    return nodo

def Create_resistor():#Crea el nodo de la resistencia
    nodo = Elementos()
    nodo.title = "Resistencia"
    nodo.type_text = "Default"+ str(len(lista_elementos))
    nodo.valor = 0
    nodo.setColor(QtGui.QColor(0, 92, 138,80))


    nodo.add_conector(name="<>")
    nodo.add_conector(name="<>",energy_o=True)

    nodo.build()
    lista_elementos.append(nodo)
    return nodo



class Createmode(QtWidgets.QWidget):#Crea la ventana y carga los elementos para poder editar el circuito
    def __init__(self):
        super(Createmode,self).__init__()

        #Cargando la Interfaz
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.stack = QtWidgets.QStackedWidget()#Stack de lo widgets principales
        self.backb = self.ui.backbutton #boton para retroceder a la ventana main
        self.backb.clicked.connect(self.Back)
        self.simularB = self.ui.simularButton#boton para empezar el modo simulación
        self.simularB.clicked.connect(self.Simulacion)
        self.button2 = self.ui.backbutton_aux
        self.button2.clicked.connect(self.Restaurar)
        self.button2.hide()

        self.scene = scene = EditScene()  # Crea la scene que guardará los gráficos
        self.contenedor = self.ui.editor #widget para insertar los gráficos
        self.simularB = self.ui.simularButton  # Boton para iniciar la simulación

        self.layout = QtWidgets.QHBoxLayout() #Layout del widget table

        self.listaElementos = ListaElementos(self)
        self.splitter = QtWidgets.QSplitter()

        self.layout.addWidget(self.splitter)
        self.contenedor.setLayout(self.layout)

        self.event_filter = EventFilter(self)


        self.scene.setSceneRect(0, 0, 999, 999)  # tamaño de la escena
        self.view = Table(self.contenedor)
        self.view.setScene(self.scene)
        self.event_filter.install(self.scene)


        #Agregando elementos nuevos a la interfaz
        self.splitter.addWidget(self.view) # Divide de manera ordenada los widgets
        self.splitter.addWidget(self.listaElementos)


        self.view.request_node.connect(self.Create_Elemento)# conecta el evento de request_ node a una función que crea un nodo


    def Back(self):#funcion para regresar a la primera pantalla
        self.listaElementos.show()
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

    def Simulacion(self):# Activa el modo simulación
        self.backb.hide()
        self.button2.show()
        self.ui.label_5.setGeometry(1035,80,123,51)
        self.ui.label_5.setText("Resistencias")
        self.ui.label_5.setFont(getFontLabel())
        self.listaElementos.hide()

        self.listaresistencias = Listaresistencias(self)
        self.listaresistencias.show()

        for elemento in lista_elementos:
            elemento.setFlag(QtWidgets.QGraphicsPathItem.ItemIsMovable,False)
            if elemento.title == "Resistencia":
                self.listaresistencias.Add_resistencia(elemento.type_text)
            for conector in elemento.conectores:
                conector.setFlag(QtWidgets.QGraphicsPathItem.ItemIsSelectable,False)
        self.listaresistencias.setListaElementos(lista_elementos)

    def Restaurar(self): # Restaura las configuraciones de los widgets
        self.button2.hide()
        self.listaresistencias.clear()
        self.listaresistencias.hide()
        for elemento in lista_elementos: # Configura los elementos para que se puedan mover o no
            elemento.setFlag(QtWidgets.QGraphicsPathItem.ItemIsMovable,True)
            for conector in elemento.conectores:
                conector.setFlag(QtWidgets.QGraphicsPathItem.ItemIsSelectable,True)


        self.backb.show()
        self.listaElementos.show()
        self.ui.label_5.setGeometry(830,80,201,51)
        self.ui.label_5.setFont(getnormalfont())
        self.ui.label_5.setText("Elementos")









