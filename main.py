from PyQt5.QtWidgets import QApplication, QVBoxLayout
from ArrowGame import ArrowGame

app = QApplication([])

game = ArrowGame()
game.changeLayout(QVBoxLayout())
game.createBoard([1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 2, 1], 2)

print("created board")
game.show()

app.exec()