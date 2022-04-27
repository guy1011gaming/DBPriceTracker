import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("DB Price Tracker")
        self.setGeometry(500, 200, 500, 400)

        self.initUI()

    def initUI(self):
        url_field = QtWidgets.QLineEdit("Enter URL", self)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()