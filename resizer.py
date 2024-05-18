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
)

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Photo Editor")
main_window.resize(900, 700)


main_window.show()
app.exec_()
