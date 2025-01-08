from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSlider, QHBoxLayout, QComboBox, QStackedLayout, QStackedWidget, QSizePolicy
from PyQt5.QtGui import QColor, QPainter, QPixmap, QLinearGradient

from brush import Brush

class ColorPicker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Color Picker")
        self.setGeometry(10, 570, 400, 400)
        self.setStyleSheet("background-color: white")

        self.colorPick = False

        self.brush = Brush()
        self.__color = QColor(255, 255, 255)

        self.boxLabel = QLabel(self)
        self.createBoxGradient(200, QColor("cyan"))

        self.circleIndicatorPixmap = self.createCircleIndicator()
        self.circleIndicatorLabel = QLabel(self)
        self.circleIndicatorLabel.setPixmap(self.circleIndicatorPixmap)
        self.circleIndicatorLabel.setStyleSheet("background: transparent; border: none;")

        self.spectrumLabel = QLabel(self)
        self.createSpectrumGradient()
        self.spectrumLabel.move(QPoint(250, 0))

        self.primColorLabel = QLabel(self)
        self.primColorLabel.move(325, 50)
        map = QPixmap(50,50)
        map.fill(QColor("black"))
        self.primColorLabel.setPixmap(map)

        self.setUpSliders()

        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.show()

    def setUpSliders(self):
        widgetContainer = QWidget(self)

        sliderLayout = QVBoxLayout(self)

        colorRepChoices = QComboBox()
        colorRepChoices.addItems(["HSV", "RGB", "CMYK", "HSL", "Overall View"])
        colorRepChoices.currentIndexChanged.connect(self.changeColorRep)
        sliderLayout.addWidget(colorRepChoices)

        self.repLayouts = QStackedLayout()

        sliderList = ["HSV", "RGB", "CMYK", "HSL"]

        
        for repType in sliderList:
            mainContainer = QWidget(self)
            mainLayout = QVBoxLayout(self)
            for char in repType:
                tempContainer = QWidget()
                rowLayout = QHBoxLayout()
                name = QLabel(char)
                slider = QSlider(Qt.Horizontal, tempContainer)
                slider.setRange(0, 360 if char == "H" else 255)
                slider.setValue(180)
                valueLabel = QLabel("128", tempContainer)
                valueLabel.setFixedWidth(40)
                slider.valueChanged.connect(
                    lambda value, label=valueLabel, context=repType, currentRep=char: 
                    self.sliderTasks(context, currentRep, value, label) 
                )

                tempContainer.setMinimumHeight(40)

                rowLayout.addWidget(name)
                rowLayout.addWidget(slider)
                rowLayout.addWidget(valueLabel)

                tempContainer.setLayout(rowLayout)
                mainLayout.addWidget(tempContainer)

            mainContainer.setLayout(mainLayout)
            self.repLayouts.addWidget(mainContainer)


        containerForStack = QWidget(self)
        containerForStack.setLayout(self.repLayouts)
        sliderLayout.addWidget(containerForStack)

        widgetContainer.setLayout(sliderLayout)
        widgetContainer.setGeometry(0, 200, 400, 200)

    def changeColorRep(self, index):
        self.repLayouts.setCurrentIndex(index)

    def sliderTasks(self, context, currentRep, value, label: QLabel):
        label.setText(str(value))

        match(context):
            case "HSV":
                hsv = self.__color.getHsv() #(h, s, v, alpha)
                if currentRep is "H":
                    self.__color.setHsv(value, hsv[1], hsv[2], hsv[3])
                    tempColor = QColor(0, 0, 0)
                    tempColor.setHsv(value, 255, 255)
                    self.createBoxGradient(200, tempColor)
                elif currentRep is "S":
                    self.__color.setHsv(hsv[0], value, hsv[2], hsv[3])
                else:
                    self.__color.setHsv(hsv[0], hsv[1], value, hsv[3])
            case "RGB":
                rgb = self.__color.getRgb()
                if currentRep is "R":
                    self.__color.setRgb(value, rgb[1], rgb[2], rgb[3])
                elif currentRep is "G":
                    self.__color.setRgb(rgb[0], value, rgb[2], rgb[3])
                else:
                    self.__color.setRgb(rgb[0], rgb[1], value, rgb[3])
            case "CMYK":
                cymk = self.__color.getCmyk()
                if currentRep is "C":
                    self.__color.setCmyk(value, cymk[1], cymk[2], cymk[3], cymk[4])
                elif currentRep is "M":
                    self.__color.setCmyk(cymk[0], value, cymk[2], cymk[3], cymk[4])
                elif currentRep is "Y":
                    self.__color.setCmyk(cymk[0], cymk[1], value, cymk[3], cymk[4])
                else:
                    self.__color.setCmyk(cymk[0], cymk[1], cymk[2], value, cymk[4])
            case "HSL":
                hsl = self.__color.getHsl() #(h, s, l, alpha)
                if currentRep is "H":
                    self.__color.setHsv(value, hsl[1], hsl[2], hsl[3])
                    tempColor = QColor(0, 0, 0)
                    tempColor.setHsl(value, 255, 255)
                    self.createBoxGradient(200, tempColor)
                elif currentRep is "S":
                    self.__color.setHsv(hsl[0], value, hsl[2], hsl[3])
                else:
                    self.__color.setHsl(hsl[0], hsl[1], value, hsl[3])
        self.changePrimaryColor()
        

    def sliderStyleSheets(self, context, currentRep):
        styleSheet = ""
        
        match(context):
            case "HSV":
                if currentRep is "H":
                    pass
                elif currentRep is "S":
                    pass
                else:
                    pass
            case "RGB":
                pass
            case "CMYK":
                pass
            case "HSL":
                pass

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
            self.circleIndicatorLabel.move(boxPos.x(), boxPos.y())
        elif self.spectrumLabel.geometry().contains(event.pos()):
            specPos = self.spectrumLabel.mapFromGlobal(event.globalPos())
            color = self.specImage.pixelColor(specPos.x(), specPos.y())
            self.changePrimaryColor()
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
                self.circleIndicatorLabel.move(boxPos.x(), boxPos.y())