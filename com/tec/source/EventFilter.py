from PySide2 import QtWidgets, QtCore

class eventFilter(QtCore.QObject):# Gestiona los eventos y los lanza
    def __init__(self,parent):
        super(eventFilter, self).__init__(parent)
        self.connection = None
        self.port = None
        self.scene = None
        self._last_selected = None
    def install(self,scene):
        self.scene = scene
        self.scene.installEventFilter(self)
    def EventFilter(self,fuente,event):# método encargado de gestionar los eventos recibidos de la Scene

        return super(eventFilter, self).eventFilter(fuente, event)