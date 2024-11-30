from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap

class Canvas(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.resize(width, height)

        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(QColor("white"))
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(460, 160, self.pixmap)

class ToolBox(QWidget):
    def __init__(self):
        super().__init__()
        self.masterLayout = QGridLayout()
        
        self.pencilButton = QPushButton("Pencil", self)
        self.pencilButton.clicked.connect(self.pencilClicked)
        self.masterLayout.addWidget(self.pencilButton)

        self.brushButton = QPushButton("Brush", self)
        self.brushButton.clicked.connect(self.brushClicked)
        self.masterLayout.addWidget(self.brushButton)

        self.boxSelButton = QPushButton("Box Selection", self)
        self.boxSelButton.clicked.connect(self.selectionClicked)
        self.masterLayout.addWidget(self.boxSelButton)

        self.elSelButton = QPushButton("Ellipse Selection", self)
        self.elSelButton.clicked.connect(self.selectionClicked)
        self.masterLayout.addWidget(self.elSelButton)

        self.fillButton = QPushButton("Fill", self)
        self.fillButton.clicked.connect(self.fillClicked)
        self.masterLayout.addWidget(self.fillButton)

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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up of overall initial GUI
        self.setStyleSheet("background-color: grey;")

        self.menu = QMenuBar

        self.canvas = Canvas(1000, 750)
        self.setCentralWidget(self.canvas)

        self.toolWindow = ToolBox()

        # Set up of brushes and tools
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

if __name__ == "__main__":
    app = QApplication([])
    mainWin = Window()
    mainWin.showMaximized()
    app.exec_()