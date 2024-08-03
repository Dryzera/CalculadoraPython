from buttons import ButtonsGrid
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from info import Info
from display import Display
from main_window import MainWindow
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication()
    setupTheme(app)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    # app.setWindowIcon(icon)

    # INFO
    info = Info('Nenhuma Conta')
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()