from PySide2 import QtWidgets, QtGui, QtCore


class Conector(QtWidgets.QGraphicsPathItem):#conectores de los nodos, permiten conectar elementos

    def __init__(self,parent):
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

        self.m_node = None
        self.connection = None  # idenfifica si existe alguna conexión

        self.text_path = QtGui.QPainterPath()

    def set_Energy(self, da_energia):
        self.energy_o = da_energia

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

    def paint(self, painter, option=None, widget=None):
        painter.setPen(QtGui.QPen(1))
        painter.setBrush(QtCore.Qt.green)
        painter.drawPath(self.path())

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.white)
        painter.drawPath(self.text_path)

    def clear_connection(self):
        if self.connection:
            self.connection.delete()

    def can_connect_to(self, port):
        print(port.getNodo(), self.getNodo())
        if not port:
            return False
        if port.getNodo() == self.getNodo():
            return False

        if self.energy_o == port.energy_o:
            return False

        return True

    def is_connected(self):
        if self.connection:
            return True
        return False

    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemScenePositionHasChanged:
            if self.connection:
                self.connection.Resetinicialfinal()

        return value
