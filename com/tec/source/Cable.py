from PySide2 import QtWidgets, QtGui, QtCore


class Cable(QtWidgets.QGraphicsPathItem):
    def __init__(self, parent):
        super(Cable, self).__init__(parent)
        self.setFlag(QtWidgets.QGraphicsPathItem.ItemIsSelectable)

        self.setPen(QtGui.QPen(QtGui.QColor(230, 219, 91, 90), 2))
        self.setBrush(QtCore.Qt.NoBrush)
        self.setZValue(-1)

        self._conectorInicial = None
        self._conectorFinal = None

        self.posinicial = QtCore.QPointF()
        self.posfinal = QtCore.QPointF()

        self._resaltar = False
        self._contienecarga = False
        self._valorcarga = 0

    def Delete(self):  # Elimina el cable

        for conector in (self._conectorInicial, self._conectorFinal):
            if conector:
                conector.cable = None
            conector = None
        self.scene().removeItem(self)

    @property
    def conectorInicial(self):
        return self._conectorInicial
    @property
    def conectorFinal(self):
        return self._conectorFinal
    @property
    def carga(self):
        return self._contienecarga
    @property
    def valorcarga(self):
        return self._valorcarga
    @property
    def getNodos(self):
        return (self._conectorInicial().getNodo(), self._conectorFinal().getNodo())

    @conectorInicial.setter
    def conectorInical(self, nodo):
        self._conectorInicial = nodo
        self._conectorInicial.cable = self
    @conectorFinal.setter
    def conectorFinal(self,nodo):
        self._conectorFinal = nodo
        self._conectorFinal.cable = self
    @carga.setter
    def carga(self, carga):
        self._contienecarga = carga
    @valorcarga.setter
    def valorcarga(self, valor):
        self._valorcarga = valor

    def Resetinicialfinal(self):
        if self._conectorInicial and not self._conectorInicial.is_output():
            aux = self._conectorFinal
            self._conectorFinal = self._conectorInicial
            self._conectorInicial = aux
        if self._conectorInicial:
            self.posinicial = self._conectorInicial.scenePos()
        if self._conectorFinal:
            self.posfinal = self._conectorFinal.scenePos()
        self.Refrescar()
    def Refrescar(self):# cambia la posición del cable y crea una pequeña curva
        path = QtGui.QPainterPath()
        path.moveTo(self.posinicial)

        dirx = self.posfinal.x() - self.posinicial.x()
        diry = self.posfinal.y() - self.posinicial.y()

        ctr1 = QtCore.QPointF(self.posinicial.x() + dirx * 0.9, self.posinicial.y())
        ctr2 = QtCore.QPointF(self.posinicial.x() + dirx * 0.9, self.posinicial.y() + diry)
        path.cubicTo(ctr1, ctr2, self.posfinal)

        self.setPath(path)
    def paint(self,painter,option=None,widget=None):#Método heredado de QGraphicsPathItem, cambia e color del trazo en pantalla segun sea la variable
        if self.isSelected() or self._resaltar:
            painter.setPen(QtGui.QPen(QtGui.QColor(173,119,12,68), 3)) #color al estar seleccionado
            #showCarga()
        else:
            painter.setPen(QtGui.QPen(QtGui.QColor(32,55,199,78), 2)) # color sin seleccionar
            #ShowCarga()off

        painter.drawPath(self.path()) # dibuja el cable
