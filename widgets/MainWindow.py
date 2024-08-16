from PySide6 import QtWidgets
from PySide6.QtCore import QSize
from widgets.SearchBar import SearchBar

APP_TITLE = "Python Weather App"


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(1280, 724))
        self.setWindowTitle(APP_TITLE)
        self.setStyleSheet("background-color: #263238")
        searchBar = SearchBar()
        self.setCentralWidget(searchBar)
