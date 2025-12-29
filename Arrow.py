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
        super().resizeEvent(ev)
        self.setIconSize(QSize(self.width(), self.height()))

    def refresh(self):
        pixmap = self.baseIcon.pixmap(self.iconSize())
        trans = QTransform()
        trans.rotate(self.direction * (360 / self.states))

        rotPixmap = pixmap.transformed(trans)
        self.setIcon(QIcon(rotPixmap))

    def changeIconSize(self, s):
        self.setIconSize(s)

    def clickAnim(self):
        thread = Thread(target=self.paintClick)
        thread.start()

    def paintClick(self):
        self.changeIconSize(self.iconSize() * 0.6)
        self.refresh()
        sleep(0.1)
        self.changeIconSize(QSize(self.width(), self.height()))
        self.refresh()