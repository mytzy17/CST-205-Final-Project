import sys
import sip #Install sip
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QVBoxLayout, QPushButton, QFileDialog, QComboBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from google.cloud import translate
from function import *
translate_client = translate.Client()
results = translate_client.get_languages()

func = ImageToText()
extractedText = "empty"
class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #self.setMinimumSize(QSize(600, 600))
        self.setWindowTitle("Image Translator")

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        label = QLabel(self)
        pixmap = QPixmap('welcome.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.button = QPushButton("Upload Image", self)
        self.uploadLabel = QLabel(self)
        self.button.clicked.connect(self.onClick)
        lay.addWidget(self.button)
        lay.addWidget(self.uploadLabel)

        self.dialog = Second()
        self.translatebtn = QPushButton("Translate", self)
        self.translatebtn.clicked.connect(self.on_click)
        self.comboBox = QComboBox()

        for lang in range(len(results)):
            self.comboBox.addItem(results[lang]['name'])

        lay.addWidget(self.translatebtn)
        lay.addWidget(self.comboBox)
        lay.addWidget(label)
        
    @pyqtSlot()
    def onClick(self):	
        fname, _ = QFileDialog.getOpenFileName(self.uploadLabel, 'Open File', '/usr/tmp', "Images (*.jpg *png)")
        extractedText = func.getText(fname) #extracted text from image is here
        print(extractedText)
        self.uploadLabel.setPixmap(QPixmap(fname))
        return extractedText

    def on_click(self):
        current_value = self.comboBox.currentText()  
        print(current_value)
        print(extractedText)
        #textFrom = onClick(self)
        #result = translate_client.detect_language(textFrom)
        #print(result['language'])
        #print(results[current_value])
        #print(func.translate(text, results[current_value]))
        self.dialog.show()


class Second ( QWidget ):
    def __init__(self):
        super ().__init__ ()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
