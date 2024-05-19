import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
)
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # Set app settings
        self.setWindowTitle("Hello App")
        # self.setWindowIcon(QIcon(":/icons/"))
        self.resize(500, 350)

        # Set Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Widgets
        self.inputField = QLineEdit()
        button = QPushButton("&Say Hello", clicked=self.sayHello)
        self.output = QTextEdit()

        # Add widgets to layout
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText(f"Hello {inputText}")


app = QApplication(sys.argv)
app.setStyleSheet(
    """
    QWidget {
        font-size: 25px;
    }
    
    QPushButton {
        font-size: 20px;
    }
"""
)

window = MyApp()
window.show()

app.exec_()
