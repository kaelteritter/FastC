import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("FastC")
        self.setFixedSize(300, 400)

        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#2b2b2b"))  # Синий цвет
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())