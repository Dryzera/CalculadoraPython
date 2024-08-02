from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout
from utils import isNumOrDot, isEmpty
from display import Display
from variables import MEDIUM_FONT_SIZE
import variables

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.configStyle()
    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.display = display

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

    
    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNumOrDot(button_text) and isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplay(
                    self._insertButtomTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)


    def _makeButtonDisplay(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    
    def _insertButtomTextToDisplay(self, button):
        button_text = button.text()
        self.display.insert(button_text)
