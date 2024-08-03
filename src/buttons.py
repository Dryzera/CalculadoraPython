from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display
from variables import MEDIUM_FONT_SIZE
from typing import TYPE_CHECKING
from styles import qss
from variables import DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.display = display
        self.info = info
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._equation = ''
        self._makeGrid()

    
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(self._equation)
        return self._equation

    
    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setStyleSheet(f'background-color: {DARKER_PRIMARY_COLOR}')
                    print(button_text, 2222222222222)

                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplay(
                    self._insertButtomTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)

    def _insertButtomTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _makeButtonDisplay(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot