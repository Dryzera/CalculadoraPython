from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QGridLayout
import variables

class ButtonsGrid(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.configStyle()
    
    def configStyle(self):
        self.setStyleSheet(f'font-size: {variables.MIDIUM_FONT_SIZE}px')