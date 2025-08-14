from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QLineEdit, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dallas College Course Availability Checker")
        layout = QVBoxLayout()

        self.label = QLabel("Are there any open seats?")
        layout.addWidget(self.label)

        input = QLineEdit()
        input.setMaxLength(7)
        input.setPlaceholderText("Enter Registration #")
        layout.addWidget(input)

        self.dropdown = QComboBox()
        layout.addWidget(self.dropdown)

        self.button = QPushButton("Check")
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def populateDropdown(self, filename: str):
        with open("prefixes.txt", 'r') as file:
            prefixes = file.readlines()
            print(f"reading {file}")
            for prefix in prefixes:
                self.dropdown.addItem(prefix)


app = QApplication(sys.argv)

window = MainWindow()
window.populateDropdown("prefixes.txt")
window.show()

app.exec()