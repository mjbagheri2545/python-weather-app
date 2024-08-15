from PySide6 import QtWidgets
from PySide6.QtCore import QSize


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, appTitle):
        super().__init__()
        self.setFixedSize(QSize(1280, 724))
        self.setWindowTitle(appTitle)
        self.setStyleSheet("background-color: #263238")
