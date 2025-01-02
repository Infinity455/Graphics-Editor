from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QColor, QPainter, QPixmap, QLinearGradient

class ColorPicker(QWidget): # TODO allows for an overall gradient of the color spectrum for choosing
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Color Picker")
        self.setGeometry(10, 570, 400, 400)
        self.setStyleSheet("background-color: white")

        label = QLabel(self)
        label.setPixmap(self.createBoxGradient(200))

        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.show()

    def createBoxGradient(self, side):
        pixmap = QPixmap(side, side)
        pixmap.fill(Qt.transparent)

        sideToSide = QLinearGradient(0, 0, side, 0)
        downToUp = QLinearGradient(0, side, 0, 0)

        sideToSide.setColorAt(0.0, QColor("white"))
        sideToSide.setColorAt(1.0, QColor("cyan"))

        downToUp.setColorAt(0.0, QColor(0, 0, 0, 255))
        # downToUp.setColorAt(0.0, QColor(0, 0, 0, 255))
        downToUp.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), sideToSide)
        painter.fillRect(pixmap.rect(), downToUp)
        painter.end()

        return pixmap