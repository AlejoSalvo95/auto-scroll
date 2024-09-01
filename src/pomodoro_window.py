from PyQt5.QtCore import QTimer, Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPalette, QColor
import sys
from utils import get_window_height
from scroll import start_scrolling

class PomodoroWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scroll Window')
        self.resize(300, 400)
        self.move(50, get_window_height() - 350)

        self.notifButton = QPushButton('Slow down', self)
        self.notifButton.clicked.connect(lambda: start_scrolling(-2, 2))

        self.notifButton1 = QPushButton('Whatsapp stickers down', self)
        self.notifButton1.clicked.connect(lambda: start_scrolling(-9, 1))

        self.notifButton2 = QPushButton('Whatsapp stickers up', self)
        self.notifButton2.clicked.connect(lambda: start_scrolling(9, 1))

        self.notifButton3 = QPushButton('Slow up', self)
        self.notifButton3.clicked.connect(lambda: start_scrolling(2, 2))


        self.notifButton4 = QPushButton('Top up', self)
        self.notifButton4.clicked.connect(lambda: start_scrolling(500, 1))
        layout = QVBoxLayout()
        layout.addWidget(self.notifButton)
        layout.addWidget(self.notifButton1)
        layout.addWidget(self.notifButton2)
        layout.addWidget(self.notifButton3)
        layout.addWidget(self.notifButton4)

        self.setLayout(layout)
