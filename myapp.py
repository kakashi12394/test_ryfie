from PyQt5.QtCore import Qt, QTime, QTimer, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.InitUI()
        self.connects()
        self.show()
        

    def InitUI(self):
        self.btn_next = QPushButton(txt_next)
        self.text_hello = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.text_hello, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)

        self.setLayout(self.layout)


    def set_appear(self):
        self.setWindowTitle('Тест Руфье')
        self.move(win_x, win_y)
        self.resize(win_width, win_height)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)


    def next_click(self):
        self.tw = SecondWin()
        self.hide()
        #self.tw.show()


app = QApplication([])
root = MainWin()
app.exec_()