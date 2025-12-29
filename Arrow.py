from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QTransform
from PyQt5.QtWidgets import QPushButton
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
        self.setFixedSize(QSize(200, 200))
        self.setIconSize(QSize(200, 200))

        self.affectedArrows = []
        self.states = states
        self.direction = direction

        self.refresh()

    def resizeEvent(self, ev):
        """Ensures the icon scales to the button size and as a square"""
        super().resizeEvent(ev)
        self.setIconSize(QSize(self.width(), self.height()))

    def refresh(self):
        """Reloads the arrow image and rotates it based on the direction"""
        pixmap = self.baseIcon.pixmap(self.iconSize())
        trans = QTransform()
        trans.rotate(self.direction * (360 / self.states))

        rotPixmap = pixmap.transformed(trans)
        self.setIcon(QIcon(rotPixmap))

    def changeIconSize(self, s):
        self.setIconSize(s)

    def clickAnim(self):
        """Adds a little click animation to the clicked button"""
        thread = Thread(target=self.paintClick)
        thread.start()

    def paintClick(self, time=0.1, mult=0.6):
        self.changeIconSize(self.iconSize() * mult)
        self.refresh()
        sleep(time)
        self.changeIconSize(QSize(self.width(), self.height()))
        self.refresh()