import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QVBoxLayout, QWidget, QInputDialog, QFileDialog
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt, pyqtSignal

from logic.commands import ConvertImageCommand
from logic.observers import ConversionNotifier

class MainWindow(QMainWindow):

    fileSelected = pyqtSignal()

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

        # Метка для отображения выбранного файла
        self.lbl_selected_file = QLabel("Файл не выбран")
        self.lbl_selected_file.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_selected_file.setWordWrap(True)

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


        # Чтобы кнопка была по центру, используем layout
        layout = QVBoxLayout()
        layout.addStretch(1)  # Добавляет растягиваемое пространство сверху
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)  # Кнопка по центру
        layout.addStretch(6)  # Добавляет растягиваемое пространство снизу

        # Создаём контейнерный виджет и устанавливаем layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)  # Устанавливаем как центральный виджет

        self.fileSelected.connect(self.changeButtonText)
        
    def the_button_was_clicked(self):
        # Открываем диалог выбора файла
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Выберите файл",
            "",  # Начальная директория (пусто = последняя использованная)
            "Все файлы (*);;Текстовые файлы (*.txt);;Изображения (*.png *.jpg *.jpeg)"
        )
        print(file_path)
        if file_path:
            self.fileSelected.emit()
    
    def changeButtonText(self):
        
        self.button.setText("Convert image")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())