import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.drawing = False
        self.lst = []

    def paintEvent(self, event):
        if self.drawing:
            self.qp = QPainter(self)
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()
            self.update()

    def draw(self, qp):
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 164, 0))
        qp.setPen(pen)
        for i in range(20):
            if len(self.lst) < 20:
                self.lst.append([randint(0, 800), randint(0, 600), randint(20, 100)])
            qp.drawEllipse(self.lst[i][0], self.lst[i][1], self.lst[i][2], self.lst[i][2])

    def run(self):
        self.drawing = True
        self.lst = []


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
