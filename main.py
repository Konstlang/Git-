import sys

from PyQt5 import uic
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circ(qp)
            qp.end()

    def draw_circ(self, qp):
        qp.setPen(QColor(255, 255, 0))
        for i in range (10):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            qp.drawEllipse(x + 50, y + 50, x + 100, y + 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())