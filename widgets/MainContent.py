from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from utilities import WeatherResponseData
from widgets.Item import Item
from typing import cast

UNITS = {
    "description": "",
    "temperature": " ℃",
    "minTemperature": " ℃",
    "maxTemperature": " ℃",
    "humidity": "%",
    "windSpeed": " m/s",
}


class MainContent(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()

        self._label = QLabel("No Information Available")
        self._label.setStyleSheet("font-size: 26px")
        self._label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._layout.addWidget(self._label)

        self._layout.setSpacing(35)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.setContentsMargins(0, 0, 50, 0)

        self._items = QHBoxLayout()
        self._items.setSpacing(25)
        self._layout.addLayout(self._items)
        for key in [
            "description",
            "temperature",
            "minTemperature",
            "maxTemperature",
            "humidity",
            "windSpeed",
        ]:
            self._items.addWidget(Item(key))

        self.setFixedWidth(1280)
        self.setLayout(self._layout)

    def setTitle(self, title: str):
        self._label.setText(title)
        self._label.repaint()

    def setItems(self, weatherResponseData: WeatherResponseData):
        for index, (key, value) in enumerate(weatherResponseData.items()):
            item = self._getItemLabel(index)
            item.setText(f"{value}{UNITS[key]}")
            item.repaint()

    def resetItems(self):
        items = cast(QHBoxLayout, self._layout.itemAt(1))
        for index in range(items.count()):
            item = self._getItemLabel(index)
            item.setText("__")
            item.repaint()

    def _getItemLabel(self, index) -> QLabel:
        return self._items.itemAt(index).widget().layout().itemAt(1).widget()
