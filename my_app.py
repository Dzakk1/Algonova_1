# # write here a code for the main app and the first screenfrom PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

# from PyQt5.QtWidgets import 

from instr import *
from second_win import *

class MainWin(QWidget):
       def __init__(self):
              super().__init__()
              self.set_appear()# mengatur seperti apa tampilan jendela
              self.initUI() # membuat dan mengkonfigurasi elemen grafis
              self.connects() # membangun hubungan antar elemen
              self.show()


       def set_appear(self): 
              # pass
              self.setWindowTitle(txt_title)
              self.resize(win_width, win_height)
              self.move(win_x, win_y)
       
       def initUI(self): 
              # pass
              self.btn_next = QPushButton(txt_next, self)
              self.hello_text = QLabel(txt_hello)
              self.instruction = QLabel(txt_instruction)


              self.layout_line = QVBoxLayout()
              self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
              self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
              self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
              self.setLayout(self.layout_line)

       def connects(self): 
              self.btn_next.clicked.connect(self.next_click)
              
       
       def next_click(self):
              self.hide()
              self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()


