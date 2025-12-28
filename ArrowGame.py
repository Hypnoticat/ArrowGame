from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QPushButton

from Arrow import Arrow
from Game import Game


class ArrowGame(QMainWindow, Game):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arrow Game")
        self.arrows = []
        self.selectedArrow = None

        self.controlDisplay = QWidget()
        self.controlLayout = QGridLayout()
        self.assocBtn = QPushButton("Associate arrows")
        self.assocBtn.setCheckable(True)
        self.assocBtn.setChecked(True)
        self.setButton = QPushButton("Choose activating button")
        self.controlLayout.addWidget(self.assocBtn)
        self.controlLayout.addWidget(self.setButton)
        self.controlDisplay.setLayout(self.controlLayout)

        self.display = QWidget()
        self.displayLayout = QHBoxLayout()
        self.displayLayout.addWidget(self.root)
        self.displayLayout.addWidget(self.controlDisplay)
        self.display.setLayout(self.displayLayout)

        self.refresh()

        self.assocBtn.clicked.connect(self.associateButtons)
        self.setButton.clicked.connect(self.resetSelection)

    def changeLayout(self, layout):
        self.chooseLayout(layout)
        self.refresh()

    def add(self, elem, x=0, y=0, colSpan=1, rowSpan=1):
        self.addElement(elem, (x, y), Qt.AlignHCenter, colSpan, rowSpan)

    def createBoard(self, states):
        w = ""
        h = 0
        while w != "0":
            w = input("How many elements are in the next row. Use a number, 0 to end.\n")
            if w.isdigit():
                if isinstance(self.layout, QGridLayout):
                    for i in range(int(w)):
                        arr = Arrow(states)
                        self.arrows.append(arr)
                        self.add(arr, i, h)
                if isinstance(self.layout, QVBoxLayout):
                    row = QHBoxLayout()
                    for i in range(int(w)):
                        arr = Arrow(states)
                        self.arrows.append(arr)
                        row.addWidget(arr)
                    self.add(row)


                # increment so we know the row has increased
                h += 1
        self.connectClicks()

    def connectClicks(self):
        for arrow in self.arrows:
            if arrow.receivers(arrow.clicked) > 0:
                arrow.disconnect()
            arrow.clicked.connect(self.turnArrows)

    def associateButtons(self):
        if not self.assocBtn.isChecked():
            self.assocBtn.setStyleSheet("background-color : green")
            for arrow in self.arrows:
                if arrow.receivers(arrow.clicked) > 0:
                    arrow.disconnect()
                arrow.clicked.connect(self.clickToConnect)
        else:
            self.assocBtn.setStyleSheet("background-color : red")
            self.connectClicks()

    def resetSelection(self):
        if self.selectedArrow is not None:
            self.selectedArrow.setStyleSheet("background-color : none")
            self.selectedArrow = None

    def turnArrows(self):
        for affArr in self.sender().affectedArrows:
            affArr.direction = (affArr.direction + 1) % (affArr.states)
            affArr.refresh()
    def clickToConnect(self):
        if self.selectedArrow is None:
            self.selectedArrow = self.sender()
            self.selectedArrow.setStyleSheet("background-color: lightblue")
            print("Selected an arrow")
        else:
            if self.sender() not in self.selectedArrow.affectedArrows:
                self.selectedArrow.affectedArrows.append(self.sender())
            print("Added an association")

    def refresh(self):
        self.display.setLayout(self.displayLayout)
        self.setCentralWidget(self.display)