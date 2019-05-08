import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QHBoxLayout, QPushButton, QComboBox


class Second ( QWidget ):
    def __init__(self):
        super ().__init__ ()


class MainWindow ( QMainWindow ):
    def __init__(self):
        super ().__init__ ()
        self.setWindowTitle ( 'Translator' )
        self.show ()
        self.button = QPushButton ( 'Click' )
        self.button.clicked.connect ( self.on_click )
        self.dialog = Second ()
        self.mainwidget = QWidget(self)
        self.combo_box = QComboBox() 
        self.combo_box.addItems(["English", "Spanish"])

        Lay = QHBoxLayout ()
        Lay.addWidget(self.button)
        Lay.addWidget(self.combo_box)
        self.mainwidget.setLayout(Lay)
        self.setCentralWidget(self.mainwidget)

        # @pyqtSlot()
    def on_click(self):
    	self.dialog.show ()


app = QApplication ( sys.argv )
win = MainWindow ()
win.show ()
sys.exit ( app.exec_ () )

