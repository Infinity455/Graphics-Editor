from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, QLabel, QAction, QStatusBar)

from brush import Brush
from canvas import Canvas
from toolbox import ToolBox
from colorPicker import ColorPicker

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
    '''