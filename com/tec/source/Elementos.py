from PySide2 import QtWidgets, QtGui, QtCore

from com.tec.source.Conectores import Conector


class Elementos(QtWidgets.QGraphicsPathItem):
    def __init__(self):
        super(Elementos, self).__init__()

        # imagenes para los elementos
        #self.resistenciaIcon = 'GUI/Resources/resistor.png'
        #self.fuenteIcon = 'GUI/Resources/power.png'

        # Propiedades de los elementos
        self.setFlag(QtWidgets.QGraphicsPathItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsPathItem.ItemIsSelectable)
        self.dir = "horizontal"

        self._title_text = None
        self._type_text = None
        self.metric = " "


        self._width = 61
        self._height = 51
        self._conectores = [] # lista de los conectores


        self.node_color = QtGui.QColor(0, 92, 138,80) # color del nodo


        self.title_path = QtGui.QPainterPath()
        self.type_path = QtGui.QPainterPath()
        self.misc_path = QtGui.QPainterPath()

        self.horizontal_margin = 30  # margen horizontal
        self.vertical_margin = 15  # margen vertical

    @property
    def title(self):
        return self._title_text

    @title.setter
    def title(self, title):
        self._title_text = title
        if self.title == "Fuente de Poder":
            self.metric = "volts"
        else:
            self.metric = "ohms"


    @property
    def type_text(self):
        return self._type_text

    @type_text.setter
    def type_text(self, type_text):
        self._type_text = type_text
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor (self, valor):
        self._valor = str(valor)

    def getGeometry(self):
        datos = [self.x(),self.y(),self._width,self._height]
        return datos

    def paint(self,painter, option=None, widget=None):  # crea el visual del nodo


        if self.isSelected():
            painter.setPen(QtGui.QPen(QtGui.QColor(241, 175, 0), 2))
            painter.setBrush(self.node_color)
        else:
            painter.setPen(self.node_color.lighter())
            painter.setBrush(self.node_color)


        painter.drawPath(self.path())

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.white)
        painter.drawPath(self.title_path)
        painter.drawPath(self.type_path)
        painter.drawPath(self.misc_path)


    def add_conector(self, name, energy_o=False, flags=0, ptr=None):  # añade un conector al elemento
        port = Conector(self,self.scene())
        port.set_energy(energy_o)
        port.set_name(name)
        port.set_node(node=self)
        port.set_port_flags(flags)
        port.set_ptr(ptr)
        #port.setcarga = self.valor

        self._conectores.append(port)#añade el conector a la lista de conectores

    def build(self):  # crea el elemento en pantalla


        self.title_path = QtGui.QPainterPath()  # reset
        self.type_path = QtGui.QPainterPath()
        self.misc_path = QtGui.QPainterPath()
        self.carga_path = QtGui.QPainterPath()

        total_width = 0
        total_height = 0
        path = QtGui.QPainterPath()  # The main path



        # Las tipografias
        title_font = QtGui.QFont("OCR A Extended", pointSize=12)
        title_type_font = QtGui.QFont("OCR A Extended", pointSize=8)
        port_font = QtGui.QFont("OCR A Extended")

        # Dimensiones del nombre
        title_dim = {
            "w": QtGui.QFontMetrics(title_font).width(self._title_text),
            "h": QtGui.QFontMetrics(title_font).height(),
        }

        title_type_dim = {
            "w": QtGui.QFontMetrics(title_type_font).width("Nombre: "+ self._type_text + " Valor: "+self._valor+" "+ self.metric ),
            "h": QtGui.QFontMetrics(title_type_font).height(),
        }

        # ancho maximo
        for dim in [title_dim["w"], title_type_dim["w"]]:
            if dim > total_width:
                total_width = dim

        # Add both the title and type height together for the total height
        for dim in [title_dim["h"], title_type_dim["h"]]:
            total_height += dim

        # Add the heigth for each of the ports
        for conector in self._conectores:
            port_dim = {
                "w": QtGui.QFontMetrics(port_font).width(conector.name()),
                "h": QtGui.QFontMetrics(port_font).height(),
            }

            if port_dim["w"] > total_width:
                total_width = port_dim["w"]

            total_height += port_dim["h"]

        # Add the margin to the total_width
        total_width += self.horizontal_margin
        total_height += self.vertical_margin

        # Draw the background rectangle
        path.addRoundedRect(-total_width / 2, -total_height / 2, total_width, total_height, 5, 5)

        # Dibuja el name
        self.title_path.addText(
            -title_dim["w"] / 2,
            (-total_height / 2) + title_dim["h"],
            title_font,
            self._title_text,
        )

        # Dibuja el tipo
        self.type_path.addText(
            -title_type_dim["w"] / 2,
            (-total_height / 2) + title_dim["h"] + title_type_dim["h"],
            title_type_font,
            "Nombre: " + self._type_text + " Valor: " + self.valor + " " + self.metric,
        )


        y = (-total_height / 2) + title_dim["h"] + title_type_dim["h"] + port_dim["h"]

        count = 1
        for conector in self._conectores:#agrega los conectores\

            if self.title == "Fuente de Poder":
                if conector.is_output():
                    conector.setPos(total_width/2, y)
                else:
                    conector.setPos(-total_width/2, y)
            else:
                if count==1 :
                    conector.setPos(-total_width/2,y)
                else:
                    conector.setPos(total_width/2,y)
            count += 1



        self.setPath(path)

        self._width = total_width
        self._height = total_height

    # Funciones de mantenimiento
    def select_connections(self, value):#Indica si se esta en estado de conecion
        for port in self._conectores:
            if port._cables:
                for cable in port._cables:
                    cable._resaltar = value
                    cable.Refrescar()

    def delete(self):
        """
        Elimina los conectores.
        """
        to_delete = []

        for port in self._conectores:
            if port._cables:
                for cable in port._cables:
                    to_delete.append(cable)

        for connection in to_delete:
            connection.delete()

        self.scene().removeItem(self)#elimina el nodo
    def Refresh(self):
        for conector in self._conectores:
            conector.Refresh()
        self.build()
    def Rotate(self):#Rota el elemento
        if self.dir == "horizontal":
            self.setRotation(90)
            self.dir = "vertical"
        elif self.dir == "vertical":
            self.setRotation(180)
            self.dir = "horizontal1"
        elif self.dir == "horizontal1":
            self.setRotation(-90)
            self.dir = "vertical1"
        else:
            self.setRotation(0)
            self.dir="horizontal"
