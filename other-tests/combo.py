import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QStackedWidget, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dropdown Example")
        self.setGeometry(100, 100, 400, 300)

        # Main layout
        mainLayout = QVBoxLayout()

        # Dropdown (QComboBox)
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Option 1", "Option 2", "Option 3"])
        self.dropdown.currentIndexChanged.connect(self.changeWidget)

        # Stacked widget to hold different pages
        self.stackedWidget = QStackedWidget()
        
        # Add pages to stacked widget
        self.stackedWidget.addWidget(QLabel("This is the content for Option 1"))
        self.stackedWidget.addWidget(QLabel("This is the content for Option 2"))
        self.stackedWidget.addWidget(QLabel("This is the content for Option 3"))

        # Add dropdown and stacked widget to layout
        mainLayout.addWidget(self.dropdown)
        mainLayout.addWidget(self.stackedWidget)

        # Set central widget
        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def changeWidget(self, index):
        """Change the displayed widget based on the dropdown selection."""
        self.stackedWidget.setCurrentIndex(index)


# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
