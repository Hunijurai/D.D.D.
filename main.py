import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.agg)
        self.paint = False

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            for i in range(3):
                self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setPen(QColor(255, 255, 0))
        a = randint(1, min([self.width(), self.height()]) // 4)
        qp.drawEllipse(randint(self.width() // 4, self.width() * 3 // 4), randint(self.height() // 4, self.height() * 3 // 4), a, a)


    def agg(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mn = Main()
    mn.show()
    sys.exit(app.exec())
