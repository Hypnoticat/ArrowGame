from PyQt5.QtWidgets import QApplication, QVBoxLayout
from ArrowGame import ArrowGame

app = QApplication([])

game = ArrowGame()
game.changeLayout(QVBoxLayout())
game.createBoard([3, 3, 3], 4)

print("created board")
game.show()

app.exec()