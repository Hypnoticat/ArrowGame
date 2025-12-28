from PyQt5.QtWidgets import QApplication, QVBoxLayout
from ArrowGame import ArrowGame

app = QApplication([])

game = ArrowGame()
game.changeLayout(QVBoxLayout())
game.createBoard(4)

print("created board")
game.show()

app.exec()