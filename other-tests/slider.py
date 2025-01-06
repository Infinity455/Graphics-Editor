import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QSlider,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class SliderDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sliders with Labels Demo")
        self.setGeometry(100, 100, 600, 400)

        # Main widget and layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        mainLayout = QVBoxLayout(centralWidget)

        # Add sliders with labels
        self.setUpSlidersWithLabels(mainLayout)

    def setUpSlidersWithLabels(self, parentLayout):
        # Create a container widget for the sliders
        sliderContainer = QWidget(self)

        # Create a vertical layout for stacking sliders
        sliderLayout = QVBoxLayout(sliderContainer)

        # Create sliders with labels
        sliders = [
            ("Hue", QSlider(Qt.Horizontal, sliderContainer)),
            ("Saturation", QSlider(Qt.Horizontal, sliderContainer)),
            ("Value", QSlider(Qt.Horizontal, sliderContainer)),
            ("Red", QSlider(Qt.Horizontal, sliderContainer)),
            ("Green", QSlider(Qt.Horizontal, sliderContainer)),
            ("Blue", QSlider(Qt.Horizontal, sliderContainer)),
        ]

        # Add each slider to the layout
        for name, slider in sliders:
            # Create horizontal layout for this slider row
            rowLayout = QHBoxLayout()

            # Create the name label
            nameLabel = QLabel(name, sliderContainer)

            # Set up the slider
            slider.setRange(0, 255)
            slider.setValue(128)  # Default value

            # Set up the value label
            valueLabel = QLabel("128", sliderContainer)
            valueLabel.setFixedWidth(40)  # Make it compact and align it neatly

            # Connect the slider's value change signal to update the value label
            slider.valueChanged.connect(lambda value, label=valueLabel: label.setText(str(value)))

            # Add widgets to the row layout
            rowLayout.addWidget(nameLabel)
            rowLayout.addWidget(slider)
            rowLayout.addWidget(valueLabel)

            # Add the row layout to the main vertical layout
            sliderLayout.addLayout(rowLayout)

        # Add the slider container layout to the parent layout
        parentLayout.addWidget(sliderContainer)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = SliderDemo()
    demo.show()
    sys.exit(app.exec_())
