from email.charset import QP
from PyQt5.QtCore import Qt, QTime, QTimer, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.InitUI()
        self.connects()
        self.show()

    def InitUI(self):
        self.txt_FIO = QLineEdit(txt_hintname)
        self.years = QLineEdit(txt_hintage)
        self.first_test = QLineEdit(txt_hinttest1)
        self.second_test = QLineEdit(txt_hinttest2)
        self.third_test = QLineEdit(txt_hinttest3)
        #кнопки
        self.start_first_test = QPushButton(txt_starttest1)
        self.start_sit = QPushButton(txt_starttest2)
        self.final_test = QPushButton(txt_starttest3)
        self.all_in_all = QPushButton(txt_sendresults)
        #текст
        self.health = QLabel(txt_title)
        self.enter_FIO = QLabel(txt_name)
        self.all_years = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)

        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
       

        #вывод на экран
        self.layout = QVBoxLayout()
        self.r_line = QHBoxLayout()

        self.r_line.addWidget(self.text_timer, alignment= Qt.AlignRight)
        self.layout.addWidget(self.health, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.enter_FIO, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.txt_FIO, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.all_years, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.years, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.start_first_test, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.first_test, alignment = Qt.AlignLeft)
        self.layout.addLayout(self.r_line)
        self.layout.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.start_sit, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.final_test, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.second_test, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.third_test, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.all_in_all, alignment = Qt.AlignCenter)

        self.setLayout(self.layout)
        

    def set_appear(self):
        self.setWindowTitle('Тест Руфье')
        self.move(win_x, win_y)
        self.resize(win_width, win_height)




    def connects(self):
        self.all_in_all.clicked.connect(self.next_click)
        self.start_first_test.clicked.connect(self.timer_test)
        self.start_sit.clicked.connect(self.timer_sits)
        self.final_test.clicked.connect(self.timer_final)

    def next_click(self):
        #self.tw = MainWin()
        self.hide()
        self.exp = Experiment(int(self.years.text()), self.first_test.text(), self.second_test.text(), self.third_test.text())
        self.fw = FinalWin(self.exp)
        
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
       global time
       time = QTime(0, 1, 0)
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer3Event)
       self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color, rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color, rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
       global time
       time = time.addSecs(-1)
       self.text_timer.setText(time.toString("hh:mm:ss"))
       if int(time.toString("hh:mm:ss")[6:8]) >= 45:
           self.text_timer.setStyleSheet("color: rgb(0,255,0)")
       elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
           self.text_timer.setStyleSheet("color: rgb(255,0,0)")
       else:
           self.text_timer.setStyleSheet("color: rgb(0,0,0)")
       self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
       if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()
        