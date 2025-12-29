from PyQt5.QtWidgets import QApplication, QVBoxLayout
from ArrowGame import ArrowGame

app = QApplication([])

game = ArrowGame()
game.changeLayout(QVBoxLayout())
game.createBoard([3, 2, 4], 16)

print("created board")
game.show()

app.exec()