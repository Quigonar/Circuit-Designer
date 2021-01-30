from PySide2 import QtWidgets, QtGui, QtCore


class Conector(QtWidgets.QGraphicsPathItem):#conectores de los nodos, permiten conectar elementos

    def __init__(self,parent,scene):
        super(Conector, self).__init__(parent)

        self.radius_ = 5
        self.margin = 2

        path = QtGui.QPainterPath()
        path.addEllipse(-self.radius_, -self.radius_, 2 * self.radius_,2 * self.radius_)  # añade el circulo para el conector
        self.setPath(path)

        self.setFlag(QtWidgets.QGraphicsPathItem.ItemSendsScenePositionChanges)
        self.font = QtGui.QFont()
        self.font_metrics = QtGui.QFontMetrics(self.font)

        self.port_text_height = self.font_metrics.height()

        self.energy_o = False  # indica si el conector lleva energía o la reccibe
        self._name = None
        self.margin = 2
        self.carga = 0

        self.m_node = None
        self._cables = []  # idenfifica si existe alguna conexión

        self.text_path = QtGui.QPainterPath()

    def set_Energy(self, salida):
        self.energy_o = salida


    def set_Name(self, name):
        self._name = name
        nice_name = self._name.replace("_", " ").title()
        self.port_text_width = self.font_metrics.width(nice_name)  # Ajusta el texto

        if self.energy_o:
            x = -self.radius_ - self.margin - self.port_text_width
            y = self.port_text_height / 4

            self.text_path.addText(x, y, self.font, nice_name)
        else:
            x = self.radius_ + self.margin
            y = self.port_text_height / 4

            self.text_path.addText(x, y, self.font, nice_name)

    def set_node(self, node):
        self.m_node = node
        if self.energy_o == True:
            if self.m_node.title != "Resistencia":
                self.carga = self.m_node.valor
    def get_node(self):
        return self.m_node

    def set_port_flags(self, flags):
        self.m_port_flags = flags

    def set_ptr(self, ptr):
        self.m_ptr = ptr

    def name(self):
        return self._name

    def is_output(self):
        return self.energy_o

    def getNodo(self):
        return self.m_node

    def getCarga(self):
        return self.carga

    def paint(self, painter, option=None, widget=None):
        painter.setPen(QtGui.QPen(1))
        painter.setBrush(QtCore.Qt.green)
        painter.drawPath(self.path())

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.white)
        painter.drawPath(self.text_path)

    def clear_connection(self):
        for cable in self._cables:
            if cable:
                cable.delete()

    def can_connect_to(self, port):
        if not port:
            return False
        if port.getNodo() == self.getNodo():
            return False

        if self.energy_o == port.energy_o:
            return False


        return True

    def is_connected(self):
        if self._cables:
            return True
        return False

    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemScenePositionHasChanged:
            for cable in self._cables:
                cable.Resetinicialfinal()
        return value

    def Refresh(self): # cambia los valores de la carga al ser editados
        if self.m_node.title != "Reisistencia":
            self.carga = self.m_node.valor
        else:
            self.carga = self.m_node.valor - 1.60
        if self.is_connected():# Si el conector esta conectado envia la energía a los cables
            if self.energy_o:
                for cable in self._cables:
                    cable.valorcarga = self.carga