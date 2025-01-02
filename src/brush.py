from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPainter, QPixmap, QCursor, QPainterPath


class Brush(QWidget):

    toolChanged = pyqtSignal()

    # Ensures class is a singleton
    _instance = None
    def __new__(current):
        if current._instance is None:
            current._instance = super().__new__(current)
        return current._instance

    def __init__(self):
        super().__init__()
        self.brush = None
        self.size = 50
        self.color = QColor(0, 0, 0)
        self.poisiton = QPoint(0, 0)
        self.shape = None
        self.setBrushType("pencil")

    def setBrushType(self, type: str):
        self.brush = type
        if not self.shape == None:
            self.shape = None
        path = QPainterPath()
        match(type):
            case "pencil":
                pixmap = QPixmap(self.size, self.size)
                pixmap.fill(Qt.transparent)

                with QPainter(pixmap) as painter:
                    painter.setBrush(Qt.transparent)
                    painter.setPen(Qt.black)
                    painter.drawRect(0, 0, self.size - 1, self.size - 1)

                self.brushForCursor = QCursor(pixmap)

                path.addRect(0, 0, self.size - 1, self.size - 1)
                self.shape = path
            case "round":
                pixmap = QPixmap(self.size, self.size)
                pixmap.fill(Qt.transparent)

                with QPainter(pixmap) as painter:
                    painter.setBrush(Qt.transparent)
                    painter.setPen(Qt.black)
                    painter.drawEllipse(0, 0, self.size - 1, self.size - 1)

                self.brushForCursor = QCursor(pixmap)

                path.addEllipse(0, 0, self.size - 1, self.size - 1)
                self.shape = path
            case _:
                print("WARNING: Brush not found")
        self.toolChanged.emit()

    def setBrushPosition(self, point: QPoint):
        self.position = point

    def getCurrentBrush(self):
        return self.brushForCursor
    
    def getShape(self):
        return self.shape
    
    def getSize(self):
        return self.size
    
    def increaseSize(self): # Increases size + resets same brush with new size
        self.size += 1
        self.setBrushType(self.brush)

    def decreaseSize(self): # Decreases size + resets same brush with new size
        self.size -= 1
        self.setBrushType(self.brush)


if __name__ == "__main__":
    pass