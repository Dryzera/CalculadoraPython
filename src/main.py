from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from info import Info
from display import Display
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    # app.setWindowIcon(icon)

    # INFO
    info = Info('Nenhuma Conta')
    window.add_Widget_V_Layout(info)

    display = Display()
    window.add_Widget_V_Layout(display)

    window.adjustFixedSize()
    window.show()
    app.exec()