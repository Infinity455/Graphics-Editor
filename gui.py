import sys
import cv2
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsView

# Class for a custom canvas widget
class Canvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.setScene(self.scene)

        self.setStyleSheet("background-color: white;")

# Class for the main window with all widgets
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        
        self.setStyleSheet("background-color: grey;")

       # Central widget and layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(layout)

        # Create canvas and limit its size
        self.canvas = Canvas()
        self.canvas.setFixedSize(400, 600)

        # Add canvas to layout with spacing
        layout.addWidget(self.canvas)
        layout.setContentsMargins(800, 20, 20, 20)
        layout.setSpacing(10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
