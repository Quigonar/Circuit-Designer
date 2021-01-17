import sys

from PySide2 import QtWidgets

from com.tec.source.GUI.Mainwindow5 import Ui_MainWindow
from com.tec.source.Createmode import Createmode
from com.tec.source.EventFilter import eventFilter

class Mainwindow(QtWidgets.QMainWindow):#Recibe como parametro la clase Mainwindow declarada del archivo .ui
    def __init__(self):
        super(Mainwindow,self).__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        _button = self.ui.createButton
        _button.clicked.connect(self.createWindow)

    def createWindow(self):#función que cambia a la ventana de creación
        widget.setCurrentIndex(widget.currentIndex()+1)


if __name__=='__main__':#Inicializa la aplicación
    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()#lista con las ventanas a mostrar
    #-----añade las ventanas a widget
    main = Mainwindow()
    widget.addWidget(main)#aniade la main window al stack
    create = Createmode()
    widget.addWidget(create)#aniade la ventana create a el stack
    create.setStack(widget)
    widget.setFixedWidth(1160)
    widget.setFixedHeight(830)
    #---------------------------
    widget.show()
    #----------


    app.exec_()#verifica que la ventana se cierre al presionar el boton "x"
