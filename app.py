from PySide6 import QtWidgets
from qt_material import apply_stylesheet
from widgets.MainWindow import MainWindow

app = QtWidgets.QApplication([])

apply_stylesheet(app, theme="dark_teal.xml")

window = MainWindow()
window.show()

app.exec()
