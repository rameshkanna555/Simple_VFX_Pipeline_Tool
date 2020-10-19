try :
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *
import Publisher


##### This class create a main window ##########


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Hhoop_publisher')
        self.setGeometry(150,150,750,380)
        self.setFixedSize(800,380)

        self.UI()

        self.show()


    def UI(self):
        self.layouts()
        self.widgets()

    def layouts(self):

        self.hlayout = QHBoxLayout()
        self.hlayout.setSpacing(0)
        self.hlayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.hlayout)


    def widgets(self):

        self.qtpublishBtn = QPushButton('QT-Publisher')
        self.qtpublishBtn.setFixedSize(400,400)
        self.qtpublishBtn.setStyleSheet("font:15px")
        self.qtpublishBtn.clicked.connect(self.qtPublish)

        # self.qtpublishBtn.setStyleSheet(" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);")


        self.finalpublishBtn = QPushButton('Final-Publisher')
        self.finalpublishBtn.setFixedSize(400,400)
        self.finalpublishBtn.setStyleSheet("font:15px")
        self.finalpublishBtn.clicked.connect(self.finalPublisher)


        self.hlayout.addWidget(self.qtpublishBtn)
        self.hlayout.addWidget(self.finalpublishBtn)

    def qtPublish(self):
        self.close()

        self.qt_publish = Publisher.QtPublisher()

    def finalPublisher(self):

        self.close()
        self.finalpublish = Publisher.FinalPublisher()
        return 0




def start():

    start.pipeline = MainWindow()
