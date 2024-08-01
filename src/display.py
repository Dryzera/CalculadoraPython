import variables
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QLineEdit

class Display(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        self.setStyleSheet(f'font-size: {variables.BIG_FONT_SIZE}px')
        self.setMinimumHeight(variables.BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[variables.TEXT_MARGIN for _ in range(4)])