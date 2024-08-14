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
        self.countdownTimer = QTimer(self)
        self.countdownTimer.timeout.connect(self.update_countdown)
        self.remainingTime = 0
        self.fast = False

    def initUI(self):
        self.setWindowTitle('Pomodoro Timer')
        self.resize(300, 100)
        self.move(50, get_window_height() - 350)

        self.notifButton = QPushButton('Slow', self)
        self.notifButton.clicked.connect(lambda: self.scroll_slow())

        self.notifButton2 = QPushButton('SFast', self)
        self.notifButton2.clicked.connect(lambda: self.scroll_fast())

        layout = QVBoxLayout()
        layout.addWidget(self.notifButton)
        layout.addWidget(self.notifButton2)

        self.setLayout(layout)

    def increase_timer(self):
        self.remainingTime += 60

    def decrease_timer(self):
        if self.remainingTime > 60:
            self.remainingTime -= 60

    def scroll_slow(self):
        self.scroll()

    def scroll_fast(self):
        self.fast = True
        self.scroll()

    def scroll(self):
        duration = self.set_main_window()
        self.countdownTimer.start(1000)
        start_scrolling()

    def set_main_window(self):
        if self.fast == True:
            duration = 900000
        else:
            duration = 5000
        self.remainingTime = duration // 1000
        return duration

    def set_notification_background(self, window, color):
        palette = window.palette()
        palette.setColor(QPalette.Window, color)
        window.setPalette(palette)

    def update_countdown(self):
        self.remainingTime -= 1

