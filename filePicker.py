#FIle Picker tester
##https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm
import sys
from PyQt5 import *
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from function import *
class filePicker(QWidget):
	def __init__(self):
		super().__init__()
		vbox = QVBoxLayout()
		self.button = QPushButton("Upload Image", self)
		self.labels = QLabel(self)
		self.button.clicked.connect(self.on_click)
		vbox.addWidget(self.button)
		vbox.addWidget(self.labels)

		self.setLayout(vbox)
	@pyqtSlot()
	def on_click(self):
            fname, _ = QFileDialog.getOpenFileName(self.labels, 'Open File', '/usr/tmp', "Images (*.jpg *.png)")
#            pixmap4 = fname.scaled(1200, 800)
            print(fname)
            self.labels.setPixmap(QPixmap(fname))


myApp = QApplication(sys.argv)
myWindow = filePicker()
myWindow.setGeometry(100, 100, 1200, 800)
myWindow.setWindowTitle("Hello")
myWindow.show()

sys.exit(myApp.exec_())

if __name__ == '__main__':
   main()


