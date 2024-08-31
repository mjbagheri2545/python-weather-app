from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QSize
from widgets.SearchBar import SearchBar
from widgets.MainContent import MainContent
from utilities import (
    LocationResponse,
    LocationData,
    getWeather,
    WeatherResponse,
)

APP_TITLE = "Python Weather App"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(1280, 724))
        self.setWindowTitle(APP_TITLE)
        self.setStyleSheet("background-color: #263238")


        self._mainContent = MainContent()
        searchBar = SearchBar(self._handleOnSearch, self._mainContent.setTitle, self._mainContent.resetItems)

        self._verticalLayout = QVBoxLayout()
        self._verticalLayout.addWidget(searchBar)
        self._verticalLayout.addWidget(self._mainContent)
        self._verticalLayout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(self._verticalLayout)

        self.setCentralWidget(widget)

    def _handleOnSearch(self, locationResponse: LocationResponse):
        if isinstance(locationResponse, Exception):
            self._mainContent.setTitle(
                "Location Not Found Or Maybe An Error Occurred During Retrieving Location Data"
            )
        else:
            self._mainContent.setTitle(
                "Retrieving Weather Data ..."
            )
            weatherResponse = getWeather(locationResponse["location"])
            self._handleWeatherResponse(weatherResponse, locationResponse)

    def _handleWeatherResponse(
        self, weatherResponse: WeatherResponse, locationData: LocationData
    ):
        if isinstance(weatherResponse, Exception):
            self._mainContent.setTitle(
                "An Error Occurred During Retrieving Weather Data"
            )
        else:
            self._mainContent.setTitle(f"{locationData["name"]}, {locationData['country']}")
            self._mainContent.setItems(weatherResponse)
