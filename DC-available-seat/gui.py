from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QStandardItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QLineEdit, QVBoxLayout, QWidget
import classFullChecker
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        self.prefix = ""
        self.regNumber = ""

        super().__init__()

        self.setWindowTitle("Dallas College Course Availability Checker")
        layout = QVBoxLayout()

        self.prefixLabel = QLabel("course prefix:")
        self.prefixDropdown = QComboBox()
        self.prefixDropdown.currentTextChanged.connect(self.prefixSelected)
        layout.addWidget(self.prefixLabel)
        layout.addWidget(self.prefixDropdown)

        self.regLabel = QLabel("registration #:")
        self.regInput = QLineEdit()
        self.regInput.setMaxLength(7)
        self.regInput.setInputMask("9999999;_")
        self.regInput.setPlaceholderText("enter 7-digit registration #")
        self.regInput.textEdited.connect(self.regNumberAdded)
        layout.addWidget(self.regLabel)
        layout.addWidget(self.regInput)

        self.checkButton = QPushButton("check availability")
        # stupid PyLance
        self.checkButton.clicked.connect(self.check) # type: ignore
        layout.addWidget(self.checkButton)

        self.availableLabel = QLabel()
        layout.addWidget(self.availableLabel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populatePrefixes(self, filename: str):
        print("adding prefixes...")
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
                    # print(f"added category {text}")
                # else:
                    # print(f"added prefix {text}")
        print("prefixes added")


    def prefixSelected(self, s):
        print(f"selected prefix: {s}")
        self.prefix = s

    def regNumberAdded(self, s):
        print(f"current registration number: {s}")
        self.regNumber = s

    def check(self):
        self.availableLabel.setText("Checking availability...")

        url = f"https://schedule.dallascollege.edu/FALL/Prefix/{self.prefix}"

        result = classFullChecker.checkAvailability(url, self.regNumber)

        if result == True:
            self.availableLabel.setText("Seat(s) available!")
        elif result == False:
            self.availableLabel.setText("No seats available :(")
        else:
            self.availableLabel.setText("Failed to retrieve results! See terminal output")



app = QApplication(sys.argv)

window = MainWindow()
window.populatePrefixes("prefixes.txt")
window.show()

app.exec()