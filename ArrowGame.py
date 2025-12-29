from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QPushButton

from Arrow import Arrow
from Game import Game

class ArrowGame(QMainWindow, Game):
    """The specific implementation of the arrow game.
    Is not made to be easily extendable;
    Instead offers all the required implementations for a short study"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arrow Game")
        # the list of arrows in order top to bottom, left to right
        self.arrows = []

        # the highlighted arrow(for assignment)
        self.selectedArrow = None

        # the controls on the right
        self.controlDisplay = QWidget()
        self.controlLayout = QGridLayout()

        # the buttons for associating connections
        self.assocBtn = QPushButton("Associate arrows")
        self.assocBtn.setCheckable(True)
        self.assocBtn.setChecked(True)
        self.setButton = QPushButton("Choose activating button")

        self.controlLayout.addWidget(self.assocBtn)
        self.controlLayout.addWidget(self.setButton)
        self.controlDisplay.setLayout(self.controlLayout)

        # set the main display widget
        self.display = QWidget()
        self.displayLayout = QHBoxLayout()
        self.displayLayout.addWidget(self.root)
        self.displayLayout.addWidget(self.controlDisplay)
        self.display.setLayout(self.displayLayout)

        # refresh the updated screen
        self.refresh()

        # add relevant functions to the buttons
        self.assocBtn.clicked.connect(self.associateButtons)
        self.setButton.clicked.connect(self.resetSelection)

    def changeLayout(self, layout):
        """Change the layout of the arrows"""
        self.chooseLayout(layout)
        self.refresh()

    def add(self, elem, x=0, y=0, colSpan=1, rowSpan=1):
        """Adds the element to the game, only need to provide the parameters that are necessary"""
        self.addElement(elem, (x, y), Qt.AlignHCenter, colSpan, rowSpan)

    def createBoard(self, rowWidths, states):
        """Iterates over each row creating the arrows and adding them to the class and screen"""
        h = 0
        for w in rowWidths:
            self.createRow(w, h, states)

            # increment so we know the row has increased
            h += 1

    def createRow(self, w, h, states):
        """Creates a row of arrows at the height specifieds"""
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

    def connectClicks(self):
        """Connects all the buttons to the turning function"""
        for arrow in self.arrows:
            if arrow.receivers(arrow.clicked) > 0:
                arrow.disconnect()
            arrow.clicked.connect(self.turnArrows)

    def associateButtons(self):
        """Selects a button to associate clicks with or the buttons that will turn when it is clicked"""
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
        """Resets the selected arrow"""
        if self.selectedArrow is not None:
            self.selectedArrow.setStyleSheet("background-color : none")
            self.selectedArrow = None

    def turnArrows(self):
        """Turns all the arrows of the selected arrow's affected arrows"""
        if isinstance(self.sender(), Arrow):
            self.sender().clickAnim()
        for affArr in self.sender().affectedArrows:
            affArr.direction = (affArr.direction + 1) % (affArr.states)
            affArr.refresh()

    def clickToConnect(self):
        """Either selects arrow if nothing is selected or associates the arrow with the previously selected arrow"""
        if isinstance(self.sender(), Arrow):
            self.sender().clickAnim()
        if self.selectedArrow is None:
            self.selectedArrow = self.sender()
            self.selectedArrow.setStyleSheet("background-color: lightblue")
            print("Selected an arrow")
        else:
            if self.sender() not in self.selectedArrow.affectedArrows:
                self.selectedArrow.affectedArrows.append(self.sender())
            print("Added an association")

    def refresh(self):
        """Refreshes the display and layouts"""
        self.display.setLayout(self.displayLayout)
        self.setCentralWidget(self.display)