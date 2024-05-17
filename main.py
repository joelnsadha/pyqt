# ----------Import modules------------#
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

# Main App Object and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My App")
main_window.resize(300, 200)


# ------------Create all app objects---#
title = QLabel("Random Words")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Choose Word")
button2 = QPushButton("Choose Word")
button3 = QPushButton("Choose Word")

# -------------All designs-------------#
# Create Layouts
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# Events


# Show/Run app
main_window.show()
app.exec_()
