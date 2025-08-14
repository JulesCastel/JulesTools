from PyQt6.QtWidgets import QApplication
import gui
import sys

def main():
    app: QApplication = QApplication(sys.argv)

    window: gui.MainWindow = gui.MainWindow()
    window.populatePrefixes("prefixes.txt")
    window.show()

    app.exec()

if __name__ == "__main__":
    main()