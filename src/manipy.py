from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, QLabel, QAction, QStatusBar)

from brush import Brush
from canvas import Canvas
from toolbox import ToolBox
from colorPicker import ColorPicker
from layers import Layers

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creating Canvas with default size
        self.canvas = Canvas(self)
        self.canvas.setMouseTracking(True)
        self.setCentralWidget(self.canvas)

        # toolbar window for mouse tracking in main window
        self.setMouseTracking(True)

        # Set up basics
        self.setUpMenuBar()
        self.setUpToolBar()
        self.setUpStatusBar()
        self.setStyleSheet("background-color: grey;")
        self.currentTool = None
        self.brush = Brush()

        # Color picker (Note 1)
        self.colorPicker = ColorPicker(self)

        # Layer Window
        self.layerWindow = Layers(self)

        # toolbar window for tools for painting
        self.toolBox = ToolBox(self)
        self.brush.toolChanged.connect(self.updateCursor)

        # Set up of brushes and tools
        self.setCursor(self.toolBox.getCurrentTool())
        self.drawing = False

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

        self.locationLabel = QLabel("0, 0")
        self.sizeLabel = QLabel(f"{self.canvas.getSize()[0]} px x {self.canvas.getSize()[1]} px")

        self.statusBar.addWidget(self.locationLabel)
        self.statusBar.addWidget(self.sizeLabel)


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



    '''
    Note 0:
    These will be moved in the future to its own file but it is simply more convenient to write here in the mean time.

    Note 1:
    It is important that any class calling the singleton brush class is initialized before the toolbox class. It is not
    completely clear to me what exactly the issue is but it may have to do with the how the cursor is setup with the
    brush class.

    Refactoring or rewriting the brush class may be something to look into in the future.

    Note 2:
    The color picker class keeps hue manually this is due to the following issues from how it was originally:
        1. Although HSV can keep its own memory so when an undefined hue (eg. black) appears it will return the last valid hue,
            HSL doesn't have this luxury and you need to keep your own to avoid the cases of an undefined hue causing issues
            (so when S = 0 or L = 0 or 255)
        2. It appears that using the graphical interface to adjust the saturation, value, or luminosity will cause the hue slider
            to slowly drift to the nearest primary color point. This is likely due to the changes causing the overall color to be
            recalculated and each time changing between color representations and causing slight rounding issues that add up.
    '''