from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QColor, QPainter, QPixmap, QLinearGradient

from brush import Brush

class ColorPicker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Color Picker")
        self.setGeometry(10, 570, 400, 400)
        self.setStyleSheet("background-color: white")

        self.brush = Brush()
        self.__color = QColor(255, 255, 255)

        self.boxLabel = QLabel(self)
        self.createBoxGradient(200, QColor("cyan"))

        self.circleIndicator = self.createCircleIndicator()
        self.cIlabel = QLabel(self)
        self.cIlabel.setPixmap(self.circleIndicator)
        self.cIlabel.setStyleSheet("background: transparent; border: none;")

        self.spectrumLabel = QLabel(self)
        self.createSpectrumGradient()
        self.spectrumLabel.move(QPoint(250, 0))

        self.primColorLabel = QLabel(self)
        self.primColorLabel.move(50, 325)
        map = QPixmap(50,50)
        map.fill(QColor("black"))
        self.primColorLabel.setPixmap(map)

        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.show()

    def createCircleIndicator(self):
        pixmap = QPixmap(10, 10)
        pixmap.fill(Qt.transparent)

        with QPainter(pixmap) as painter:
            painter.setBrush(Qt.transparent)
            painter.setPen(Qt.black)
            painter.drawEllipse(0, 0, 9, 9)

        return pixmap

    def createBoxGradient(self, side, hue):
        pixmap = QPixmap(side, side)
        pixmap.fill(Qt.transparent)

        sideToSide = QLinearGradient(0, 0, side, 0)
        downToUp = QLinearGradient(0, side, 0, 0)

        sideToSide.setColorAt(0.0, QColor("white"))
        sideToSide.setColorAt(1.0, hue)

        downToUp.setColorAt(0.0, QColor(0, 0, 0, 255))
        downToUp.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), sideToSide)
        painter.fillRect(pixmap.rect(), downToUp)
        painter.end()

        self.boxImage = pixmap.toImage()
        self.boxLabel.setPixmap(pixmap)
    
    def createSpectrumGradient(self):
        pixmap = QPixmap(50, 200)
        pixmap.fill(Qt.transparent)

        gradient = QLinearGradient(0, 0, 0, 200)

        gradient.setColorAt(0.0, QColor("white"))
        gradient.setColorAt(1.0, QColor("cyan"))

        gradient.setColorAt(0.0, QColor("red"))
        gradient.setColorAt(0.16, QColor("yellow"))
        gradient.setColorAt(0.33, QColor("green"))
        gradient.setColorAt(0.5, QColor("cyan"))
        gradient.setColorAt(0.66, QColor("blue"))
        gradient.setColorAt(0.83, QColor("magenta"))
        gradient.setColorAt(1.0, QColor("red"))

        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), gradient)
        painter.end()

        self.specImage = pixmap.toImage()
        self.spectrumLabel.setPixmap(pixmap)

    def getColor(self):
        return self.__color
    
    def changePrimaryColor(self):
        map = QPixmap(50,50)
        map.fill(self.__color)
        self.primColorLabel.setPixmap(map)
        self.brush.setColor(self.__color)
    
    def mousePressEvent(self, event):
        self.colorPick = True
        if self.boxLabel.geometry().contains(event.pos()):
            boxPos = self.boxLabel.mapFromGlobal(event.globalPos())
            self.__color = self.boxImage.pixelColor(boxPos.x(), boxPos.y())
            self.changePrimaryColor()
            self.cIlabel.move(boxPos.x(), boxPos.y())
        elif self.spectrumLabel.geometry().contains(event.pos()):
            specPos = self.spectrumLabel.mapFromGlobal(event.globalPos())
            color = self.specImage.pixelColor(specPos.x(), specPos.y())
            self.createBoxGradient(200, color)

    def mouseMoveEvent(self, event):
        if self.colorPick:
            if self.spectrumLabel.geometry().contains(event.pos()):
                specPos = self.spectrumLabel.mapFromGlobal(event.globalPos())
                color = self.specImage.pixelColor(specPos.x(), specPos.y())
                self.createBoxGradient(200, color)
            elif self.boxLabel.geometry().contains(event.pos()):
                boxPos = self.boxLabel.mapFromGlobal(event.globalPos())
                self.__color = self.boxImage.pixelColor(boxPos.x(), boxPos.y())
                self.changePrimaryColor()
                self.cIlabel.move(boxPos.x(), boxPos.y())