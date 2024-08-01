import variables
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.infoStyle()

    def infoStyle(self):
        self.setStyleSheet(f'font-size: {variables.SMALL_FONT_SIZE}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)