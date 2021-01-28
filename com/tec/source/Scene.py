from PySide2 import QtWidgets

class EditScene(QtWidgets.QGraphicsScene):# Muestra el QGraphic Widget

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        # envia el item a estas cordenadas
        item = self.itemAt(event.scenePos())

        if item.setAcceptDrops == True:
            # pasa las cordenadas del evento al item
            try:
                item.dropEvent(event)
            except RuntimeError:
                pass  # This will supress a Runtime Error generated when dropping into a widget with no ProxyWidget

    def dragMoveEvent(self, event):
        event.acceptProposedAction()