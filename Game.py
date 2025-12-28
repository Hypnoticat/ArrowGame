from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = None
        self.root = QWidget()

    def chooseLayout(self, layout):
        self.layout = layout
        self.gameRefresh()

    def addElement(self, elem, location, alignment, colSpan=1, rowSpan=1):
        if isinstance(self.layout, QGridLayout):
            self.layout.addWidget(elem, location[1], location[0], rowSpan, colSpan, alignment)
            self.root.setLayout(self.layout)
        if isinstance(self.layout, QVBoxLayout):
            self.layout.addLayout(elem, alignment)
            self.root.setLayout(self.layout)
        else:
            print("Layout of type " + str(type(self.layout)) + " is not supported")

    def gameRefresh(self):
        self.root.setLayout(self.layout)