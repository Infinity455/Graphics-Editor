from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class ToolWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tool Window")
        self.resize(400, 300)

        # Create a QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.addTab("Selection Tools", QLabel("Tools for selecting objects"))
        self.addTab("Brush Tools", QLabel("Tools for painting and brushes"))
        self.addTab("Settings", QLabel("Configuration and settings"))

    def addTab(self, title, content_widget):
        """Add a new tab to the tool window."""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(content_widget)
        tab.setLayout(layout)
        self.tabs.addTab(tab, title)

if __name__ == "__main__":
    app = QApplication([])
    tool_window = ToolWindow()
    tool_window.show()
    app.exec()
