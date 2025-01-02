from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QLinearGradient, QColor
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QConicalGradient, QBrush

class SpectrumGradient:
    def createConicalSpectrumGradient(size):
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.transparent)

        gradient = QConicalGradient(size / 2, size / 2, 0)
        gradient.setColorAt(0.0, QColor("red"))
        gradient.setColorAt(0.16, QColor("yellow"))
        gradient.setColorAt(0.33, QColor("green"))
        gradient.setColorAt(0.5, QColor("cyan"))
        gradient.setColorAt(0.66, QColor("blue"))
        gradient.setColorAt(0.83, QColor("magenta"))
        gradient.setColorAt(1.0, QColor("red"))

        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), gradient)
        painter.end()

        return pixmap
    
    def createSpectrumGradient(width, height):
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.transparent)

        gradient = QLinearGradient(0, 0, width, 0)

        gradient.setColorAt(0.0, QColor("red"))
        gradient.setColorAt(0.16, QColor("yellow"))
        gradient.setColorAt(0.33, QColor("green"))
        gradient.setColorAt(0.5, QColor("cyan"))
        gradient.setColorAt(0.66, QColor("blue"))
        gradient.setColorAt(0.83, QColor("magenta"))
        gradient.setColorAt(1.0, QColor("red"))

        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), gradient)
        painter.end()

        return pixmap
    
    def createBoxGradient(side):
        pixmap = QPixmap(side, side)
        pixmap.fill(Qt.transparent)

        sideToSide = QLinearGradient(0, 0, side, 0)
        downToUp = QLinearGradient(0, side, 0, 0)

        sideToSide.setColorAt(0.0, QColor("white"))
        sideToSide.setColorAt(1.0, QColor("cyan"))

        downToUp.setColorAt(0.0, QColor(0, 0, 0, 255))
        downToUp.setColorAt(0.5, QColor(0, 0, 0, 170))
        downToUp.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), sideToSide)
        painter.fillRect(pixmap.rect(), downToUp)
        painter.end()

        return pixmap

# Example usage
if __name__ == "__main__":
    app = QApplication([])
    label = QLabel()
    # spectrum = SpectrumGradient.createConicalSpectrumGradient(500)
    # spectrum = SpectrumGradient.createSpectrumGradient(500, 800)
    spectrum = SpectrumGradient.createBoxGradient(500)
    label.setPixmap(spectrum)
    label.show()
    app.exec_()
