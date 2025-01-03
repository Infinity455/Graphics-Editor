from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

from brush import Brush

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

        self.pickerButton = QPushButton("Color Picker", self)
        self.pickerButton.clicked.connect(self.pickerClicked)
        self.masterLayout.addWidget(self.pickerButton, 2, 1)

        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.show()

    def getCurrentTool(self): # The choice of creating this method over subclassing ToolBox is in account that brushes aren't the only tools
        return self.brushControl.getCurrentBrush()

    def pencilClicked(self):
        self.brushControl.setBrushType("pencil")

    def brushClicked(self):
        self.brushControl.setBrushType("round")

    def selectionClicked(self):
        button = self.sender()
        selectType = button.text()
        if selectType == "Box Selection":
            pass
        elif selectType == "Ellipse Selection":
            pass

    def fillClicked(self):
        pass

    def pickerClicked(self):
        pass


if __name__ == "__main__":
    pass