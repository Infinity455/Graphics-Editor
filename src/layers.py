from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class Layers(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(1650, 200, 200, 500)
        self.setStyleSheet("background-color: white;")

        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.show()
