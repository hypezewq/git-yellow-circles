from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow
import sys
from random import randint

class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def initUI(self):
        self.setupUi(self)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        for circle in self.circles:
            x, y, r, color = circle
            qp.setBrush(QColor(*color))
            qp.drawEllipse(x, y, r, r)

        qp.end()

    def draw_circle(self):
        x = randint(10, self.width() - 20)
        y = randint(50, self.height() - 40)
        r = randint(10, 100)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append((x, y, r, color))
        self.update()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YellowCircles()
    window.show()
    sys.exit(app.exec())