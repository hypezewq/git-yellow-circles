from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys
from random import randint

class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        for circle in self.circles:
            x, y, r = circle
            qp.setBrush(QColor("yellow"))
            qp.drawEllipse(x, y, r, r)

        qp.end()

    def draw_circle(self):
        x = randint(10, self.width() - 20)
        y = randint(50, self.height() - 40)
        r = randint(10, 100)
        self.circles.append((x, y, r))
        self.update()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YellowCircles()
    window.show()
    sys.exit(app.exec())