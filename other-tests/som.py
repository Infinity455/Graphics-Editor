import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar

# Attempt to create working status bar
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Status Bar Example")
        self.setGeometry(100, 100, 600, 400)
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.status_bar.showMessage("Ready", 5000)
        
        permanent_label = QLabel("Permanent Info")
        self.status_bar.addPermanentWidget(permanent_label)
        
        self.dynamic_label = QLabel("Dynamic Info")
        self.status_bar.addWidget(self.dynamic_label)
        
        self.update_status_bar()

    def update_status_bar(self):
        self.dynamic_label.setText("Updated Dynamic Info")
        self.status_bar.showMessage("Performing a task...", 3000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
