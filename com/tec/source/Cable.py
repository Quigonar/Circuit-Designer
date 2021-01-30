from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QPointF


class Cable(QtWidgets.QGraphicsPathItem):

    def __init__(self, parent):
        super(Cable, self).__init__(parent)
        self.setFlag(QtWidgets.QGraphicsPathItem.ItemIsSelectable)
        #self.setFlag(QtWidgets.QGraphicsPathItem.ItemSendsScenePositionChanges)

        self.setPen(QtGui.QPen(QtGui.QColor(188, 19, 207), 2))
        self.setBrush(QtCore.Qt.NoBrush)
        self.setZValue(-1)

        self._conectorInicial = None
        self._conectorFinal = None

        self.posinicial = QtCore.QPointF()
        self.posfinal = QtCore.QPointF()

        self._resaltar = False
        self._contienecarga = False
        self._valorcarga = 0

        self.fuente = ""
        self.mitad = []
        self.childs = []

    def delete(self):  # Elimina el cable
        try:
            for conector in (self._conectorInicial, self._conectorFinal):
                aux = conector._cables
                if conector:
                    if self.childs:
                        for child in self.childs:
                            child.delete()
                    self.childs = []
                    try:
                        conector._cables.remove(self)
                    except ValueError:
                        print("Error")
                conector = None
        except AttributeError:
            print("Error")
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
    def conectorInicial(self, nodo):
        self._conectorInicial = nodo
        self._conectorInicial._cables.append(self)
        self.valorcarga = self.conectorInicial.getCarga()
        #agrega los conectores al elemento
#

    @conectorFinal.setter
    def conectorFinal(self,nodo):
        self._conectorFinal = nodo
        self._conectorFinal._cables.append(self)


    @carga.setter
    def carga(self, carga):
        self._contienecarga = carga
    @valorcarga.setter
    def valorcarga(self, valor):
        self._valorcarga = valor

    def Resetinicialfinal(self):
        if self.conectorInicial and not self.conectorInicial.is_output():
            aux = self.conectorFinal
            self.conectorFinal = self.conectorInicial
            self.conectorInicial = aux
        if self.conectorInicial:
            self.posinicial = self.conectorInicial.scenePos()
        if self.conectorFinal:
            self.posfinal = self.conectorFinal.scenePos()
        if self.fuente:
            self.posinicial = QPointF(self.fuente.mitad[0],self.fuente.mitad[1])
        if self.childs:
            for child in self.childs:
                child.Resetinicialfinal()
        self.Refrescar()

    def ResetFromCable(self,dir,item):

        if self.conectorInicial and not self.conectorInicial.is_output():
            aux = self.conectorFinal
            self.conectorFinal = self.conectorInicial
            self.conectorInicial = aux
        if self.conectorFinal:
            self.posfinal = self.conectorFinal.scenePos()
        self.posinicial = dir
        self.fuente = item
        self.fuente.childs.append(self)
        self.Refrescar()

    def Refrescar(self):# cambia la posición del cable y crea una pequeña curva

        path = QtGui.QPainterPath()
        path.moveTo(self.posinicial)

        dirx = self.posfinal.x() - self.posinicial.x()
        diry = self.posfinal.y() - self.posinicial.y()

        self.mitad = [(self.posinicial.x()+(dirx/2)),self.posinicial.y()+(diry/2)]

        path.lineTo(self.posfinal)

        self.setPath(path)


    def paint(self,painter,option=None,widget=None):#Método heredado de QGraphicsPathItem, cambia e color del trazo en pantalla segun sea la variable

        if self.isSelected() or self._resaltar:
            painter.setPen(QtGui.QPen(QtGui.QColor(173,119,12,68), 3)) #color al estar seleccionado

        else:
            painter.setPen(QtGui.QPen(QtGui.QColor(188, 19, 207,78), 2)) # color sin seleccionar

        painter.drawPath(self.path()) # dibuja el cable
    """""
    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemScenePositionHasChanged:
            for child in self.childs:
                child.Resetinicialfinal()
        return value
    """