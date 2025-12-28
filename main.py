from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QSizePolicy
from PyQt5.QtGui import QIcon

app = QApplication([])

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = None
        self.setWindowTitle("Game")
        self.root = QWidget()

    def chooseLayout(self, layout):
        self.layout = layout
        self.refresh()

    def addElement(self, elem, location, alignment):
        if isinstance(self.layout, QGridLayout):
            self.layout.addWidget(elem, location[1], location[0], alignment)
            self.root.setLayout(self.layout)
        else:
            print("Layout of type " + str(type(self.layout)) + " is not supported")

    def refresh(self):
        self.setCentralWidget(self.root)

class ArrowGame(Game):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arrow Game")

    def addArrow(self, x, y):
        self.addElement(Arrow("Icons/darkarrow.png"), (x, y), Qt.AlignHCenter)

class Arrow(QPushButton):
    def __init__(self, iconPath):
        super().__init__()
        self.setIcon(QIcon("Icons/darkarrow.png"))

        self.setText("")
        self.setFlat(True)
        self.setStyleSheet("border: none; padding: 0px;")
        self.setFixedSize(QSize(200, 200))

    def resizeEvent(self, ev):
        super().resizeEvent(ev)
        self.setIconSize(QSize(self.width(), self.height()))

game = ArrowGame()

game.chooseLayout(QGridLayout())
game.addArrow(0, 0)
game.addArrow(1, 0)
game.addArrow(2, 0)
game.addArrow(0, 1)

game.show()

app.exec()