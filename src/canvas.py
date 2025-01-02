# ONLY PyQt imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPainter, QPixmap, QPainterPath

# Other project imports
from brush import Brush

class Canvas(QWidget):
    def __init__(self, parent=None, width=1000, height=750):
        super().__init__(parent)
        self.setSize(width, height)
        self.initOrigin = (460, 160)
        self.move(self.initOrigin[0], self.initOrigin[1])

        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(QColor("white"))

        self.brush = Brush()

    def addLayer():
        pass

    def removeLayer():
        pass

    def setSize(self, width, height):
        self.resize(width, height)
        
    def getEdges(self):
        # returns a tuple of QPoints of each edge of the canvas
        return (self.geometry().bottomLeft(), self.geometry().bottomRight(), self.geometry().topLeft(), self.geometry().topRight())
    
    def getSides(self):
        # returns a tuple of the sides (xLeft, yTop, xRight, yBottom)
        return self.geometry().getRect()
    
    def getBoundaries(self):
        return self.geometry()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.initOrigin[0], self.initOrigin[1], self.pixmap)

    def toolPaint(self, position):
        ogShape = self.brush.getShape()
        brushSize = self.brush.getSize()
        localPos = self.mapFromGlobal(position)
        xNorm = localPos.x() - self.initOrigin[0] - (int)(brushSize/2)
        yNorm = localPos.y() - self.initOrigin[1] - (int)(brushSize/2)
        shape = QPainterPath(ogShape)
        shape.translate(xNorm, yNorm)
        with QPainter(self.pixmap) as painter:
            painter.setBrush(Qt.black)
            painter.setPen(Qt.transparent)
            painter.drawPath(shape)
        self.update()


if __name__ == "__main__":
    pass