import sys

from PyQt5 import QtWidgets

from com.tec.source.GUI.Mainwindow5 import Ui_MainWindow
from com.tec.source.Createmode import Createmode





class Mainwindow(QtWidgets.QMainWindow):#Recibe como parametro la clase Mainwindow declarada del archivo .ui
    def __init__(self):
        super(Mainwindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        button = self.ui.createButton
        button.clicked.connect(self.createWindow)

    def createWindow(self):
        create = Createmode()
        create.setStack(widget)
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)


if __name__=='__main__':
    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()#lista con las ventanas a mostrar
    main = Mainwindow()
    widget.addWidget(main)
    widget.setFixedWidth(1160)
    widget.setFixedHeight(830)

    widget.show()
    #----------


    app.exec_()#verifica que la ventana se cierre al presionar el boton "x"
