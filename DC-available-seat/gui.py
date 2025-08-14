from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QStandardItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QLineEdit, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dallas College Course Availability Checker")
        layout = QVBoxLayout()

        self.prefixLabel = QLabel("course prefix:")
        self.dropdown = QComboBox()
        layout.addWidget(self.prefixLabel)
        layout.addWidget(self.dropdown)

        self.regLabel = QLabel("registration #")
        self.input = QLineEdit()
        self.input.setMaxLength(7)
        self.input.setPlaceholderText("enter registration #")
        layout.addWidget(self.regLabel)
        layout.addWidget(self.input)

        self.button = QPushButton("check availability")
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populateDropdown(self, filename: str):
        self.dropdown.addItem("select course prefix")
        # PyLance again being weird the hinting, this line is fine dammit!!
        # PyQt gives the QComboBox (dropdown) its model() at runtime, so the type hinting is just wrong here
        placeholder = self.dropdown.model().item(0) # type: ignore
        placeholder.setFlags(Qt.ItemFlag.NoItemFlags)

        with open(filename, 'r') as file:
            for line in file:
                text = line.strip()
                if not text:
                    continue

                self.dropdown.addItem(text)
                idx = self.dropdown.count() - 1
                prefix = self.dropdown.model().item(idx) # type: ignore

                if any(char.islower() for char in text):
                    prefix.setFlags(Qt.ItemFlag.NoItemFlags)
                    font = prefix.font()
                    font.setBold(True)
                    prefix.setFont(font)


app = QApplication(sys.argv)

window = MainWindow()
window.populateDropdown("prefixes.txt")
window.show()

app.exec()