from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    
    label1 = QLabel('Texto')
    window.add_Widget_V_Layout(label1)

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    # app.setWindowIcon(icon)

    window.adjustFixedSize()
    window.show()
    app.exec()