from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QLabel, QGridLayout, 
                             QPushButton, QVBoxLayout, QBoxLayout, QAction)
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap, QCursor

class Canvas(QWidget):
    def __init__(self, parent=None, width=1000, height=750):
        super().__init__(parent)
        self.setSize(width, height)
        self.initOrigin = (460, 160)
        self.move(self.initOrigin[0], self.initOrigin[1])

        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(QColor("white"))

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

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.initOrigin[0], self.initOrigin[1], self.pixmap)

class ToolBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
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

    def pencilClicked(self):
        pass
    def brushClicked(self):
        pass
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
    def __init__(self):
        super().__init__()
        self.brush = None
        self.size = 50
        self.color = QColor(0, 0, 0)
        self.poisiton = QPoint(0, 0)
        self.setBrushType("pencil")

    def setBrushType(self, type: str):
        self.brush = type
        match(type):
            case "pencil":
                pixmap = QPixmap(self.size, self.size)
                pixmap.fill(Qt.transparent)

                painter = QPainter(pixmap)
                painter.setBrush(QColor(255, 0, 0, 100))
                painter.setPen(QColor(0, 0, 0))
                painter.drawRect(0, 0, self.size - 1, self.size - 1)
                painter.end()

                self.brushForCursor = QCursor(pixmap)
                print("HELLO")
            case "round":
                self.brush = QRect()
            case _:
                print("WARNING: Brush not found")

    def setBrushPosition(self, point: QPoint):
        self.position = point

    def getCurrentBrush(self):
        return self.brushForCursor
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        
        x, y = self.position.x, self.position.y
        painter.drawRect(x - 25, y - 25, 50, 50)

class ColorPicker(): # TODO allows for an overall gradient of the color spectrum for choosing
    def __init__():
        pass

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up basics
        self.setUpMenuBar()
        self.setUpToolBar()
        self.setUpStatusBar()
        self.setStyleSheet("background-color: grey;")
        self.brushSingle = Brush()

        # Creating Canvas with default size
        self.canvas = Canvas(self)
        self.canvas.setMouseTracking(True)
        self.setCentralWidget(self.canvas)
        
        # toolbar window for mouse tracking in main window
        self.setMouseTracking(True)

        self.locationLabel = QLabel(self)
        self.locationLabel.setText("0, 0")
        self.locationLabel.setWindowFlags(self.locationLabel.windowFlags() | Qt.Tool)
        self.locationLabel.setGeometry(10, 200, 100, 30)
        self.locationLabel.show()

        # side layout to initialize locationLabel at
        self.sideLayout = QVBoxLayout()
        self.sideLayout.addWidget(self.locationLabel)

        # toolbar window for tools for painting
        self.toolWindow = ToolBox(self)

        # Set up of brushes and tools
        self.setCursor(self.brushSingle.getCurrentBrush())
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

    def mouseMoveEvent(self, event):
        position = event.pos()
        x = position.x()
        y = position.y()

        self.locationLabel.setText(f"{x}, {y}")    

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
        pass

    def setUpToolBar(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    mainWin = Window()
    mainWin.showMaximized()
    app.exec_()