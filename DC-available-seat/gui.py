from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QStandardItem
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QComboBox, QLineEdit, QVBoxLayout, QWidget
from typing import Optional
import classFullChecker

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        self.prefix: str = ""
        self.regNumber: str = ""

        super().__init__()

        self.setWindowTitle("Dallas College Course Availability Checker")
        layout: QVBoxLayout = QVBoxLayout()

        self.prefixLabel: QLabel = QLabel("course prefix:")
        self.prefixDropdown: QComboBox = QComboBox()
        self.prefixDropdown.currentTextChanged.connect(self.prefixSelected)
        layout.addWidget(self.prefixLabel)
        layout.addWidget(self.prefixDropdown)

        self.regLabel: QLabel = QLabel("registration #:")
        self.regInput: QLineEdit = QLineEdit()
        self.regInput.setMaxLength(7)
        self.regInput.setInputMask("9999999;_")
        self.regInput.setPlaceholderText("enter 7-digit registration #")
        self.regInput.textEdited.connect(self.regNumberAdded)
        layout.addWidget(self.regLabel)
        layout.addWidget(self.regInput)

        self.checkButton: QPushButton = QPushButton("check availability")
        # stupid PyLance
        self.checkButton.clicked.connect(self.check) # type: ignore
        layout.addWidget(self.checkButton)

        self.availableLabel: QLabel = QLabel()
        layout.addWidget(self.availableLabel)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populatePrefixes(self, filename: str) -> None:
        print("adding prefixes...")
        self.prefixDropdown.addItem("select course prefix")
        # PyLance again being weird with the hinting, this line is fine dammit!!
        # PyQt gives the QComboBox (prefixDropdown) its model() at runtime, so the type hinting is just wrong here
        placeholder: QStandardItem = self.prefixDropdown.model().item(0) # type: ignore
        placeholder.setFlags(Qt.ItemFlag.NoItemFlags)

        with open(filename, 'r') as file:
            for line in file:
                text: str = line.strip()
                if not text:
                    continue

                self.prefixDropdown.addItem(text)
                idx: int = self.prefixDropdown.count() - 1
                prefix: QStandardItem = self.prefixDropdown.model().item(idx) # type: ignore

                if any(char.islower() for char in text):
                    prefix.setFlags(Qt.ItemFlag.NoItemFlags)
                    font: QFont = prefix.font()
                    font.setBold(True)
                    prefix.setFont(font)
                    # print(f"added category {text}")
                # else:
                    # print(f"added prefix {text}")
        print("prefixes added")


    def prefixSelected(self, s: str) -> None:
        print(f"selected prefix: {s}")
        self.prefix = s

    def regNumberAdded(self, s: str) -> None:
        print(f"current registration number: {s}")
        self.regNumber = s

    def check(self) -> None:
        self.availableLabel.setText("Checking availability...")

        url: str = f"https://schedule.dallascollege.edu/FALL/Prefix/{self.prefix}"

        result: Optional[bool] = classFullChecker.checkAvailability(url, self.regNumber)

        if result == True:
            self.availableLabel.setText("Seat(s) available!")
        elif result == False:
            self.availableLabel.setText("No seats available :(")
        else:
            self.availableLabel.setText("Failed to retrieve results! See terminal output")