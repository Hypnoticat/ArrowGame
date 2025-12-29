from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLayout


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = None
        self.root = QWidget()

    def chooseLayout(self, layout):
        """Set the layout for the game"""
        self.layout = layout
        self.gameRefresh()

    def addElement(self, elem, location, alignment, colSpan=1, rowSpan=1):
        """Add an element to the game board"""
        if isinstance(self.layout, QGridLayout):
            self.layout.addWidget(elem, location[1], location[0], rowSpan, colSpan, alignment)
            self.root.setLayout(self.layout)
        if isinstance(self.layout, QVBoxLayout):
            self.layout.addLayout(elem, alignment)
            self.root.setLayout(self.layout)
        else:
            print("Layout of type " + str(type(self.layout)) + " is not supported")

    def gameRefresh(self):
        """Refresh the game board layout"""
        self.root.setLayout(self.layout)

    def resetBoard(self):
        """Reset the game board layout"""
        self.clearLayout(self.layout)

        self.gameRefresh()

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            elif item.layout():
                self.clearLayout(item.layout())