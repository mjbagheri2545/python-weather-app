from PySide6 import QtWidgets
from qt_material import apply_stylesheet
from widgets import MainWindow, SearchBar
from config import CONFIG

app = QtWidgets.QApplication([])
apply_stylesheet(app, theme="dark_teal.xml")
window = MainWindow.MainWindow(CONFIG.APP_TITLE)
searchBar = SearchBar.SearchBar()
window.setCentralWidget(searchBar)
window.show()

app.exec()
