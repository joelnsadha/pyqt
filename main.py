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

my_words = [
    "hello",
    "goodbye",
    "test",
    "app",
    "python",
    "pyqt",
    "tall",
    "here",
]

# -------------All designs-------------#
# Create Layouts
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# add title text to row1
row1.addWidget(title, alignment=Qt.AlignCenter)

# Add labels tto row2
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

# add buttons to row3
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

# Add rows to master layout
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)
# Events


# Show/Run app
main_window.show()
app.exec_()
