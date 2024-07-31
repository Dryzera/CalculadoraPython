from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, *kwargs)
    
        self.cw = QWidget()
        self._v_layout = QVBoxLayout()

        self.cw.setLayout(self._v_layout)    
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora')
        
    def add_Widget_V_Layout(self, widget: QWidget):
        self._v_layout.addWidget(widget)
        
    def adjustFixedSize(self):
        # ultimos ajustes
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        