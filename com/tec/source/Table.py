from PySide2 import QtCore, QtGui, QtWidgets, QtOpenGL
from PySide2.QtCore import QRect

from com.tec.source.Cable import Cable
from com.tec.source.Elementos import Elementos
import sys


class Table(QtWidgets.QGraphicsView):  # widget que contiene los elementos gráficos
    _background_C = QtGui.QColor(164, 199, 227, 89)  # color del fonde de la tabla

    _grid_litle = QtGui.QPen(QtGui.QColor(230, 195, 116, 90), 0.5)  # color cuadros internos
    _grid_large = QtGui.QPen(QtGui.QColor(66, 102, 153, 60), 1.0)  # color cuadros externos

    _grid_size_little = 15  # tamaño cuadros internos
    _grid_size_large = 150  # tamaño cuadros externos

    _zoom = 0.0020

    request_node = QtCore.Signal(str)  # señales o eventos en la interfaz

    def __init__(self, parent):  # code from https://github.com/bhowiebkr/logic-node-editor.git
        super(Table, self).__init__(parent)
        # Configuración gráfica
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self._manipulationMode = 0

        gl_format = QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers)
        gl_format.setSamples(10)
        gl_widget = QtOpenGL.QGLWidget(gl_format)

        self.currentScale = 1
        self._pan = False
        self._pan_start_x = 0
        self._pan_start_y = 0
        self._numScheduledScalings = 0
        self.lastMousePos = QtCore.QPoint()

        self.setViewport(gl_widget)

        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def drawBackground(self, painter, rect):  # método de QGraphicsview
        painter.fillRect(rect, self._background_C)  # agrega el color del fondo

        left = int(rect.left()) - (int(rect.left()) % self._grid_size_little)
        top = int(rect.top()) - (int(rect.top()) % self._grid_size_little)

        gridlines = []  # array con las lineas de la cuadrícula

        # Lineas internas eje y
        painter.setPen(self._grid_litle)  # añade el color a las lineas internas
        y = float(top)

        while y < float(rect.bottom()):
            gridlines.append(QtCore.QLine(rect.left(), int(y), rect.right(), int(y)))  # añade las lineas de el eje y
            y += self._grid_size_little
        painter.drawLines(gridlines)

        # Lineas internas eje x
        gridLines = []
        painter.setPen(self._grid_litle)
        x = float(left)
        while x < float(rect.right()):
            gridLines.append(QtCore.QLineF(x, rect.top(), x, rect.bottom()))
            x += self._grid_size_little
        painter.drawLines(gridLines)

        left = int(rect.left()) - (int(rect.left()) % self._grid_size_large)
        top = int(rect.top()) - (int(rect.top()) % self._grid_size_large)

        # Lineas externas eje y
        gridLines = []
        painter.setPen(self._grid_large)
        y = top
        while y < rect.bottom():
            gridLines.append(QtCore.QLineF(rect.left(), y, rect.right(), y))
            y += self._grid_size_large
        painter.drawLines(gridLines)

        # lineas externas eje x
        gridLines = []
        painter.setPen(self._grid_large)
        x = left
        while x < rect.right():
            gridLines.append(QtCore.QLineF(x, rect.top(), x, rect.bottom()))
            x += self._grid_size_large
        painter.drawLines(gridLines)

        return super(Table, self).drawBackground(painter, rect)

    def wheelEvent(self, event):  # método heredado de QGraphicsview
        # disabilita el panning
        if self._pan:
            return

        num_degrees = event.delta() / 8.0
        num_steps = num_degrees / 5.0
        self._numScheduledScalings += num_steps

        if self._numScheduledScalings * num_steps < 0:  # si cambia la dirección de la rueda
            self._numScheduledScalings = num_steps  # resetea la lista

        self.anim = QtCore.QTimeLine(350)
        self.anim.setUpdateInterval(20)

        self.anim.valueChanged.connect(self.scaling_time)
        self.anim.finished.connect(self.anim_finished)
        self.anim.start()

    def scaling_time(self, x):  # método heredado de QGraphicsview
        factor = 1.0 + self._numScheduledScalings / 300.0

        self.currentScale *= factor

        self.scale(factor, factor)

    def contextMenuEvent(self, event):
        pos = self.mapFromGlobal(QtGui.QCursor.pos())
        item = self.itemAt(event.pos())

        if item:
            if isinstance(item, Elementos):
                menu = QtWidgets.QMenu()

                edit_data = QtWidgets.QAction("Configuración", self)
                eliminar = QtWidgets.QAction("Eliminar", self)
                menu.addAction(edit_data)
                menu.addAction(eliminar)

                action = menu.exec_(self.mapToGlobal(pos))


                if action == edit_data:

                    wid = QtWidgets.QDialog(self)
                    wid.setWindowTitle("Configuración")
                    wid.setAutoFillBackground(True)

                    button = QtWidgets.QPushButton("ACEPTAR")
                    button2 = QtWidgets.QPushButton("Rotar")
                    label = QtWidgets.QLabel(item.title)

                    layout = QtWidgets.QVBoxLayout()
                    layout.addWidget(label)

                    name = item.type_text
                    editname = QtWidgets.QLineEdit()
                    editname.setText(name)

                    valor = item.valor
                    editvalor = QtWidgets.QLineEdit()
                    editvalor.setText(str(valor))

                    layout.addWidget(editname)
                    if item.title !="Resistencia":
                        layout.addWidget(editvalor)
                    layout.addWidget(button)
                    layout.addWidget(button2)
                    wid.setLayout(layout)
                    wid.setGeometry(int(item.x()), int(item.y()) - 50, 200, 50)


                    button.clicked.connect(lambda: self.ChangeData(editname.text(), editvalor.text(), item, wid))
                    button2.clicked.connect(lambda: self.Rotate(item))
                    wid.show()

                if action == eliminar:
                    item.delete()

            if isinstance(item,Cable):
                menu = QtWidgets.QMenu()
                valor = item.valorcarga
                carga = QtWidgets.QAction(str(valor), self)
                corriente = QtWidgets.QAction(str(item.corriente))
                menu.addAction(carga)
                menu.addAction(corriente)
                action = menu.exec_(self.mapToGlobal(pos))

    def ChangeData(self, name, valor, item,widget):  # Cambia los datos de los elementos

        if item.title != "Resistencia":
            item.valor = int(valor)
        item.type_text = name
        item.Refresh()
        widget.close()

    def Rotate(self,item):#Rota el elemento
        item.Rotate()

    def anim_finished(self):  # método que reduce el numero de scalas en el widget
        if self._numScheduledScalings > 0:
            self._numScheduledScalings -= 1
        else:
            self._numScheduledScalings += 1

    def dragEnterEvent(self, e):  # método que obtiene la información mime
        if e.mimeData().hasFormat("text/plain"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        drop_node_name = e.mimeData().text()
        self.request_node.emit(drop_node_name)

    def mousePressEvent(self, event):  # método heredado de Graphic view/entradas del mouse
        if event.button() == QtCore.Qt.MiddleButton:  # permite mover la vista de los gráficos
            self._pan = True
            self._pan_start_x = event.x()
            self._pan_start_y = event.y()
            self.setCursor(QtCore.Qt.ClosedHandCursor)

        return super(Table, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):  # método heredado de Graphic view
        if event.button() == QtCore.Qt.MiddleButton:
            self._pan = False
            self.setCursor(QtCore.Qt.ArrowCursor)

        return super(Table, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):  # método heredado de Graphic view/ función para el zoom en la Table
        if self._pan:
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - (event.x() - self._pan_start_x)
            )

            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - (event.y() - self._pan_start_y)
            )

            self._pan_start_x = event.x()
            self._pan_start_y = event.y()

        return super(Table, self).mouseMoveEvent(event)
