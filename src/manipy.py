from PyQt5.QtCore import Qt, QRect, QPoint, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QLabel, QGridLayout, 
                             QPushButton, QVBoxLayout, QHBoxLayout, QAction, QStatusBar)
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap, QCursor, QPainterPath, QLinearGradient, QBrush

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

class ToolBox(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.brushControl = Brush()
        self.move(10, 200)

        self.setStyleSheet("background-color: white;")
        self.masterLayout = QGridLayout()
        self.setLayout(self.masterLayout)
        
        self.pencilButton = QPushButton("Pencil", self)
        self.pencilButton.clicked.connect(self.pencilClicked)
        self.masterLayout.addWidget(self.pencilButton, 0, 0)

        self.brushButton = QPushButton("Brush", self)
        self.brushButton.clicked.connect(self.brushClicked)
        self.masterLayout.addWidget(self.brushButton, 0, 1)

        self.boxSelButton = QPushButton("Box Selection", self)
        self.boxSelButton.clicked.connect(self.selectionClicked)
        self.masterLayout.addWidget(self.boxSelButton, 1, 0)

        self.elSelButton = QPushButton("Ellipse Selection", self)
        self.elSelButton.clicked.connect(self.selectionClicked)
        self.masterLayout.addWidget(self.elSelButton, 1, 1)

        self.fillButton = QPushButton("Fill", self)
        self.fillButton.clicked.connect(self.fillClicked)
        self.masterLayout.addWidget(self.fillButton, 2, 0)

        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.show()

    def getCurrentTool(self): # The choice of creating this method over subclassing ToolBox is in account that brushes aren't the only tools
        return self.brushControl.getCurrentBrush()

    def pencilClicked(self):
        self.brushControl.setBrushType("pencil")

    def brushClicked(self):
        self.brushControl.setBrushType("round")

    def selectionClicked(self):
        button = app.sender()
        selectType = button.text()
        if selectType == "Box Selection":
            pass
        elif selectType == "Ellipse Selection":
            pass

    def fillClicked(self):
        pass

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
        downToUp.setColorAt(2.0, QColor(0, 0, 0, 255))
        downToUp.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), sideToSide)
        painter.fillRect(pixmap.rect(), downToUp)
        painter.end()

        return pixmap

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create
        # Set up basics
        self.setUpMenuBar()
        self.setUpToolBar()
        self.setUpStatusBar()
        self.setStyleSheet("background-color: grey;")
        self.currentTool = None
        self.brush = Brush()

        # Creating Canvas with default size
        self.canvas = Canvas(self)
        self.canvas.setMouseTracking(True)
        self.setCentralWidget(self.canvas)
        
        # toolbar window for mouse tracking in main window
        self.setMouseTracking(True)

        # side layout to initialize locationLabel at
        self.sideLayout = QVBoxLayout()
        self.sideLayout.addWidget(self.locationLabel)

        # toolbar window for tools for painting
        self.toolBox = ToolBox(self)
        self.brush.toolChanged.connect(self.updateCursor)

        # Set up of brushes and tools
        self.setCursor(self.toolBox.getCurrentTool())
        self.drawing = False

        # Color picker
        self.colorPicker = ColorPicker(self)

    def setUpMenuBar(self):
        self.menuBar = QMenuBar()
        self.menuBar.setStyleSheet("background-color: white;")

        fileMenu = QMenu("File", self)
        newAction = QAction("New", self)
        openAction = QAction("Open", self)
        saveAction = QAction("Save", self)
        saveAsAction = QAction("Save As", self)
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)

        self.menuBar.addMenu(fileMenu)
        self.setMenuBar(self.menuBar)

    def setUpStatusBar(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setStyleSheet("background-color: white;")

        self.locationLabel = QLabel(self)
        self.locationLabel.setText("0, 0")

        self.statusBar.addPermanentWidget(self.locationLabel)


    def setUpToolBar(self):
        pass

    def mouseMoveEvent(self, event):
        position = event.globalPos()
        x = position.x()
        y = position.y()

        self.locationLabel.setText(f"{x}, {y}")

        if self.drawing:
            self.canvas.toolPaint(position)

    def mousePressEvent(self, event):
        position = event.globalPos()
        x = position.x()
        y = position.y()

        self.drawing = True
        self.canvas.toolPaint(position)

    def mouseReleaseEvent(self, event):
        self.drawing = False

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key_Plus:
                self.brush.increaseSize()
            case Qt.Key_Minus:
                self.brush.decreaseSize()

    def updateCursor(self):
        self.setCursor(self.toolBox.getCurrentTool()) 

if __name__ == "__main__":
    app = QApplication([])
    mainWin = Window()
    mainWin.showMaximized()
    app.exec_()