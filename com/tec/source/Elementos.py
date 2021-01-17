from PyQt5.QtWidgets import QGraphicsItem
import itertools

class Elementos(QGraphicsItem):
    def __init__(self):
        QGraphicsItem.__init__(self)
        self.resistenciaIcon = 'GUI/Resources/resistor.png'
        self.fuenteIcon = 'GUI/Resources/power.png'



