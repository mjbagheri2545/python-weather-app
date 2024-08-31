from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from utilities import getLocation, LocationResponse
from typing import Callable, TypedDict

Loc = TypedDict("Loc", {"lat": str, "lon": str})


class SearchBar(QWidget):
    def __init__(
        self,
        handleOnSearch: Callable[[LocationResponse | None], None],
        setTitle: Callable[[str], None],
        resetItems: Callable[[], None],
    ):
        super().__init__()

        self._handleOnSearch = handleOnSearch
        self._setTitle = setTitle
        self._resetItems = resetItems

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
        searchInput.setPlaceholderText("Enter Your City Name")
        self._searchInput = searchInput

        layout = QHBoxLayout()
        layout.addWidget(searchInput)
        layout.addWidget(searchButton)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 30, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedHeight(200)

        self.setLayout(layout)

    def _search(self):
        searchText = self._searchInput.text()
        if searchText:
            self._searchButton.setDisabled(True)
            self._searchButton.repaint()
            self._setTitle("Retrieving Location Data ...")
            self._resetItems()
            locationResponse = getLocation(searchText)
            self._handleOnSearch(locationResponse)
            self._searchButton.setDisabled(False)
            self._searchButton.repaint()
            self._searchInput.setText("")
