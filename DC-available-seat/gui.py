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
        self.prefixDropdown = QComboBox()
        layout.addWidget(self.prefixLabel)
        layout.addWidget(self.prefixDropdown)

        self.regLabel = QLabel("registration #")
        self.regInput = QLineEdit()
        self.regInput.setMaxLength(7)
        self.regInput.setPlaceholderText("enter registration #")
        layout.addWidget(self.regLabel)
        layout.addWidget(self.regInput)

        self.checkButton = QPushButton("check availability")
        layout.addWidget(self.checkButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populatePrefixes(self, filename: str):
        self.prefixDropdown.addItem("select course prefix")
        # PyLance again being weird with the hinting, this line is fine dammit!!
        # PyQt gives the QComboBox (prefixDropdown) its model() at runtime, so the type hinting is just wrong here
        placeholder = self.prefixDropdown.model().item(0) # type: ignore
        placeholder.setFlags(Qt.ItemFlag.NoItemFlags)

        with open(filename, 'r') as file:
            for line in file:
                text = line.strip()
                if not text:
                    continue

                self.prefixDropdown.addItem(text)
                idx = self.prefixDropdown.count() - 1
                prefix = self.prefixDropdown.model().item(idx) # type: ignore

                if any(char.islower() for char in text):
                    prefix.setFlags(Qt.ItemFlag.NoItemFlags)
                    font = prefix.font()
                    font.setBold(True)
                    prefix.setFont(font)


app = QApplication(sys.argv)

window = MainWindow()
window.populatePrefixes("prefixes.txt")
window.show()

app.exec()