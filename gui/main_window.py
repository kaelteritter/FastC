import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, 
     QPushButton, QVBoxLayout, QWidget
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

from logic.commands import ConvertImageCommand
from logic.observers import ConversionNotifier

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("FastC")
        self.setFixedSize(300, 400)

        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#2b2b2b"))  # Синий цвет
        self.setPalette(palette)

        # Создаём кнопку
        self.button = QPushButton("select image")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.button.setStyleSheet("""
            QPushButton {
                background-color: #7f7f7f;  /* Синий цвет */
                color: #2b2b2b;
                border: none;
                border-radius: 5px;  /* Закруглённые углы */
                padding: 10px 20px;  /* Внутренние отступы */
                font-size: 16px;  /* Размер шрифта */
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #6e6e6e;  /* Темнее при наведении */
            }
            QPushButton:pressed {
                background-color: #5a5a5a;  /* Ещё темнее при нажатии */
            }
        """)

        self.button.setFixedSize(150, 170)

        # Создаём текстовое поле
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Введите сообщение...")
        self.text_input.setStyleSheet("""
            QLineEdit {
                background-color: #444;
                color: white;
                border: 1px solid #555;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        self.text_input.returnPressed.connect(self.on_enter_pressed)

        # Чтобы кнопка была по центру, используем layout
        layout = QVBoxLayout()
        layout.addStretch(1)  # Добавляет растягиваемое пространство сверху
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)  # Кнопка по центру
        layout.addStretch(6)  # Добавляет растягиваемое пространство снизу

        # Создаём контейнерный виджет и устанавливаем layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)  # Устанавливаем как центральный виджет
    
    def the_button_was_clicked(self):
        command = ConvertImageCommand("simple", ConversionNotifier, "file.web")
        command.execute()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())