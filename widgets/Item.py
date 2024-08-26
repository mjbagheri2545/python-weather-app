from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import Qt
from typing import TypedDict, Any

TITLES = {
    "description": "Description",
    "temperature": "Temperature",
    "minTemperature": "Min Temperature",
    "maxTemperature": "Max Temperature",
    "humidity": "Humidity",
    "windSpeed": "Wind Speed",
}


class Item(QWidget):
    def __init__(self, key: str):
        super().__init__()

        self._key = key
        title = QLabel(TITLES[self._key])
        title.setStyleSheet("font-size: 20px")
        self._value = QLabel("__")
        self._value.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addWidget(self._value)
        layout.setSpacing(15)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)
