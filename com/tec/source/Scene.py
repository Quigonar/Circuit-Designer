from PySide2 import QtWidgets, QtGui

class Scene(QtWidgets.QGraphicsScene):# Muestra el QGraphic Widget
    def dragEnterEvent(self, e):
        e.acceptProposedAction()

    def dropEvent(self, e):
        # envia el item a estas cordenadas
        item = self.itemAt(e.scenePos())
        if item.setAcceptDrops == True:
            # pasa las cordenadas del evento al item
            try:
                item.dropEvent(e)
            except RuntimeError:
                pass  # This will supress a Runtime Error generated when dropping into a widget with no ProxyWidget

    def dragMoveEvent(self, e):
        e.acceptProposedAction()