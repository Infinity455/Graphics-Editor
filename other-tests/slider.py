import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class MyApp(object):    
    def __init__(self):
        super(MyApp, self).__init__()                
        self.mainWidget = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setStyleSheet(self.stylesheet())

        self.mainLayout.addWidget(self.slider)
        self.mainWidget.show()
        sys.exit(app.exec_())

    def stylesheet(self):
        return """
            QSlider::groove:horizontal {
                background: white;
                height: 40px;
            }

            QSlider::sub-page:horizontal {
                background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
                    stop: 0 #66e, stop: 1 #bbf);
                background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                    stop: 0 #bbf, stop: 1 #55f);
                height: 40px;
            }

            QSlider::add-page:horizontal {
                background: #fff;
                height: 40px;
            }

            QSlider::handle:horizontal {
                background: #bbf;
                border: 0px;
                width: 0px;
                margin-top: 0px;
                margin-bottom: 0px;
                border-radius: 0px;
            }
        """

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MyApp()

