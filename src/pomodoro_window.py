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
        self.resize(300, 100)
        self.move(50, get_window_height() - 350)

        self.notifButton = QPushButton('Slow', self)
        self.notifButton.clicked.connect(lambda: start_scrolling(-1, 1))

        self.notifButton2 = QPushButton('Fast', self)
        self.notifButton2.clicked.connect(lambda: start_scrolling(-1, 0.5))

        layout = QVBoxLayout()
        layout.addWidget(self.notifButton)
        layout.addWidget(self.notifButton2)

        self.setLayout(layout)
