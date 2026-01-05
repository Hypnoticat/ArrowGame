from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QTransform
from PyQt5.QtWidgets import QPushButton, QSizePolicy
from time import sleep
from threading import Thread

class Arrow(QPushButton):
    def __init__(self, states, direction=0):
        super().__init__()
        self.baseIcon = QIcon("Icons/darkarrow.png")
        self.setIcon(QIcon("Icons/darkarrow.png"))

        self.setText("")
        #self.setFlat(True)
        self.setStyleSheet("border: none; padding: 0px;")
        #self.setFixedSize(QSize(100, 100))
        #self.setIconSize(QSize(100, 100))

        self.setMinimumSize(QSize(0, 0))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.affectedArrows = []
        self.states = states
        self.direction = direction

        self.refresh()

    def refresh(self):
        """Reloads the arrow image and rotates it based on the direction"""
        pixmap = self.baseIcon.pixmap(self.iconSize())
        trans = QTransform()
        trans.rotate(self.direction * (360 / self.states))

        rotPixmap = pixmap.transformed(trans)
        self.setIcon(QIcon(rotPixmap))

    def clickAnim(self):
        """Adds a little click animation to the clicked button"""
        thread = Thread(target=self.paintClick)
        thread.start()

    def paintClick(self, time=0.1, mult=0.6):
        self.setIconSize(self.iconSize() * mult)
        self.refresh()
        sleep(time)
        self.setIconSize(QSize(self.width(), self.height()))
        self.refresh()

    def resizeEvent(self, ev):
        size = min(self.width(), self.height())
        self.setIconSize(QSize(size, size))
        self.refresh()
        super().resizeEvent(ev)

    def sizeHint(self):
        return QSize(1, 1)

    def minimumSizeHint(self):
        return QSize(1, 1)
