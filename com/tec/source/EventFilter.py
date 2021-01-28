from PySide2 import QtWidgets, QtCore

from com.tec.source.Conectores import Conector
from com.tec.source.Cable import Cable
from com.tec.source.Elementos import Elementos

class EventFilter(QtCore.QObject):# Gestiona los eventos y los lanza

    def __init__(self,parent):
        super(EventFilter, self).__init__(parent)
        self.cable = None
        self.conector = None
        self.scene = None
        self._last_selected = None


    def install(self,scene):
        self.scene = scene #ventana a la que se atenderá
        self.scene.installEventFilter(self)

    def item_at(self,position): #Encuentra elementos en la Table
        items = self.scene.items(QtCore.QRectF(position - QtCore.QPointF(1, 1), QtCore.QSizeF(3, 3)))
        if items:
            return items[0]
        return None

    def eventFilter(self,watched,event):# método encargado de gestionar los eventos recibidos de la Scene
        if type(event) == QtWidgets.QWidgetItem:
            return False

        if event.type() == QtCore.QEvent.GraphicsSceneMousePress:#EVENTOS relacionados con el mouse

            if event.button() == QtCore.Qt.LeftButton:#AL presionar click izquierdo
                item = self.item_at(event.scenePos())#detecta en que scena se creo el evento

                if isinstance(item,Conector):#si se toca un conector
                    self.cable = Cable(None)

                    self.scene.addItem(self.cable)
                    self.conector = item

                    self.cable.posinicial = item.scenePos()
                    self.cable.posfinal = event.scenePos()
                    self.cable.Refrescar()
                    return True
                elif isinstance(item,Cable):# si se elige un cable
                    self.cable = Cable(None)
                    self.cable.posinicial = item.posinicial
                    self.scene.addItem(self.cable)

                    self.conector = item.posinicial

                    self.cable.posfinal = event.scenePos()
                    self.cable.Resetinicialfinal()
                    return True
                elif isinstance(item,Elementos):
                    if self._last_selected:
                        try:
                            self._last_selected.select_connections(False)
                        except RuntimeError:
                            pass
                else:
                    try:
                        if self._last_selected:
                            self._last_selected.select_connections(False)
                    except RuntimeError:
                        print("Error")
                    self._last_selected = None
            elif event.button() == QtCore.Qt.RightButton:
                pass

        elif event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Delete:# si se presiona delete se eliminan todos los elementos seleccionados
                for item in self.scene.selectedItems():

                    if isinstance(item,(Conector,Elementos)):
                        item.delete()
                return True

        elif event.type() ==QtCore.QEvent.GraphicsSceneMouseMove: #detecta el movimiento del mouse/ mueve el cable
            if self.cable:
                self.cable.posfinal = event.scenePos()
                self.cable.Refrescar()
                return True

        elif event.type() == QtCore.QEvent.GraphicsSceneMouseRelease:# AL soltar el mouse
            if self.cable and event.button() == QtCore.Qt.LeftButton:
                item = self.item_at(event.scenePos())

                #Conectando al conector
                if isinstance(item,Conector):
                    if self.conector.can_connect_to(item):
                        print("COnectando")

                        #Elimina la conexión anterior del puerto
                        if item.connection:
                            item.connection.Delete()

                        #elimina las conexiones anteriores
                        self.conector.clear_connection()
                        item.clear_connection()

                        self.cable._conectorInicial = self.conector
                        self.cable._conectorFinal = item

                        self.cable.Resetinicialfinal()
                        self.cable = None
                    else:
                        self.cable.Delete()
                        self.cable = None
                if self.cable:#elimina la conexión
                    self.cable.Delete()
                self.cable = None
                self.conector = None
                return True
        return super(EventFilter, self).eventFilter(watched, event)