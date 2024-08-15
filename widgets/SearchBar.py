from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QHBoxLayout


class SearchBar(QWidget):
    def __init__(self):
        super().__init__()
        searchButton = QPushButton("Search")
        searchButton.setFixedSize(90, 50)
        searchButton.setStyleSheet(
            """background-color:#0ea5e9; color: #fff;border: 0; border-radius: 0px;border-top-right-radius: 12px;border-bottom-right-radius: 12px;"""
        )
        searchInput = QLineEdit()
        searchInput.setFixedHeight(50)
        searchInput.setStyleSheet(
            """color: #fff;border: 2px solid #455a64;border-right: 0;border-radius: 0px; border-top-left-radius: 12px;border-bottom-left-radius: 12px; """
        )
        searchInput.setPlaceholderText("Enter Country, State, City ...")
        layout = QHBoxLayout()
        layout.addWidget(searchInput)
        layout.addWidget(searchButton)
        layout.setSpacing(0)
        self.setMaximumWidth(590)
        self.setLayout(layout)
