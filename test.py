# Import modules
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QComboBox,
)

# Configure app objects & settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Photo Editor")
main_window.resize(900, 700)


# Create layouts


# Create design aspects
btn_folder = QPushButton("Folder")
file_list = QListWidget()


btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpness")
grey = QPushButton("B/W")
saturation = QPushButton("Saturation")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

# Dripdown box
filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpness")
filter_box.addItem("B/W")
filter_box.addItem("Saturation")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

# Add design to layout


# Events

main_window.show()
app.exec_()
