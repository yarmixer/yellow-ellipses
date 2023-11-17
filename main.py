import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class GitExample(QMainWindow):
    def __init__(self):
        super(self).__init__()
        uic.loadUi('UI.ui', self)
        self.clicked = False
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.clicked = True
        self.repaint()

    def paintEvent(self, event):
        if not self.clicked:
            return
        r = random.randint(1, 300)

        qp = QPainter()
        qp.begin(self)
        c1, c2, c3 = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)

        color = QColor(c1, c2, c3)
        qp.setBrush(color)

        qp.drawEllipse(10, 50, r, r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = GitExample()
    fm.show()
    sys.exit(app.exec_())
