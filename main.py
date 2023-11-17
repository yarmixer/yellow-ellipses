import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class GitExample(QMainWindow):
    def __init__(self):
        super().__init__()
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
        r = random.randint(1, 500)

        qp = QPainter()
        qp.begin(self)

        color = QColor(255, 255, 0)
        qp.setBrush(color)

        qp.drawEllipse(10, 50, r, r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = GitExample()
    fm.show()
    sys.exit(app.exec_())
