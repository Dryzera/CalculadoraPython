from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display
from variables import MEDIUM_FONT_SIZE
from typing import TYPE_CHECKING
from styles import qss
from variables import DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR
import math

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
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._equation = ''
        self._op = None
        self._left = None
        self._right = None
        self._equationInitialValue = 'Sua conta'
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
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertButtomTextToDisplay,button)
                button.clicked.connect(slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'D':
            slot = self._makeSlot(self.display.clear, button)
            self._connectButtonClicked(button, self._clear)


        if text in '/*-+^':
            self._connectButtonClicked(button, self._makeSlot(self._operatorClicked))
            
        if text == '=':
            self._connectButtonClicked(button, self._makeSlot(self._operatorClicked))
            

    def _insertButtomTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    
    def _clear(self):
        self._op = None
        self._left = None
        self._right = None
        self._equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            return
        
        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self._equation = f'{self._left} {self._op} --'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return
        
        self._right = float(displayText)
        self._equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            print('Zero Division Error')
        except OverflowError:
            print('Número muito grande')

            self.display.clear()
            self.info.setText(f'{self.equation} = {result}')
            self._left = result
            self._right = None