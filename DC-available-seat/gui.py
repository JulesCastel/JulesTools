from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dallas College Course Availability Checker")

        button = QPushButton("Check")
        button.setCheckable(True)
        button.clicked.connect(self.clicked)

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(button)

    def clicked(self):
        print("clicked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()