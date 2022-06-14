from ctypes import alignment
from email.charset import QP
from this import s
from PyQt5.QtCore import Qt, QTime, QTimer, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()

        self.set_appear()

        self.exp = exp

        self.InitUI()

        self.show()

    def set_appear(self):
        self.setWindowTitle('Тест Руфье')
        self.move(win_x, win_y)
        self.resize(win_width, win_height)


    def InitUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line)


    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "нет данных для такого возраста"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
               return txt_res1
            elif self.index >= 17 and self.index <= 20.9:
                return txt_res2
            elif self.index >= 12 and self.index <= 16.9:
                return txt_res3
            elif self.index >= 6.5 and self.index <= 11.9:
                return txt_res4
            elif self.index <= 6.4:
                return txt_res5
        
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5 and self.index <= 19.4:
                return txt_res2
            elif self.index >= 10.5 and self.index <= 15.4:
                return txt_res3
            elif self.index >= 5 and self.index <= 10.4:
                return txt_res4
            elif self.index <= 4.9:
                return txt_res5
        
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index <= 17.9:
                return txt_res2
            elif self.index >= 9 and self.index <= 13.9:
                return txt_res3
            elif self.index >= 3.5 and self.index <= 8.9:
                return txt_res4
            elif self.index <= 3.4:
                return txt_res5

        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5 and self.index <= 16.4:
                return txt_res2
            elif self.index >= 7.5 and self.index <= 12.4:
                return txt_res3
            elif self.index >= 2 and self.index <= 7.4:
                return txt_res4
            elif self.index <= 1.9:
                return txt_res5

        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index <= 14.9:
                return txt_res2
            elif self.index >= 6 and self.index <= 10.9:
                return txt_res3
            elif self.index >= 0.5 and self.index <= 5.9:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5