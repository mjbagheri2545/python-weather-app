from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from utilities import getWeather

class SearchBar(QWidget):
    def __init__(self):
        super().__init__()

        searchButton = QPushButton("Search")
        searchButton.setFixedSize(90, 50)
        searchButton.setStyleSheet(
            """
                                   QPushButton {
                                   background-color:#0ea5e9; 
                                   color: #fff;
                                   border: 0;
                                   border-radius: 0px;
                                   border-top-right-radius: 12px;
                                   border-bottom-right-radius: 12px;
                                   }
                                   QPushButton:hover {
                                   background-color:#2bb3f3; 
                                   }
                                   QPushButton:disabled {
                                   background-color:rgba(255, 255, 255, 30%); 
                                   }
                                   """
        )
        searchButton.clicked.connect(self._search)
        searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self._searchButton = searchButton

        searchInput = QLineEdit()
        searchInput.setFixedHeight(50)
        searchInput.setMaximumWidth(500)
        searchInput.setStyleSheet(
            """color: #fff;border: 2px solid #455a64;border-right: 0;border-radius: 0px; border-top-left-radius: 12px;border-bottom-left-radius: 12px; """
        )
        searchInput.setPlaceholderText("Enter Country, State, City ...")
        self._searchInput = searchInput

        layout = QHBoxLayout()
        layout.addWidget(searchInput)
        layout.addWidget(searchButton)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 30, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def _search(self):
        searchText = self._searchInput.text()
        if searchText:
            self._searchButton.setDisabled(True)
            getWeather(searchText)
            self._searchButton.setDisabled(False)
