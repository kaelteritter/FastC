import unittest
from unittest.mock import patch
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt

from gui.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])
    
    def test_button_click(self):
        """Тест нажатия кнопки"""
        # Создаем окно с подменой метода ДО инициализации
        with patch.object(MainWindow, 'the_button_was_clicked') as mock_method:
            window = MainWindow()
            button = window.button
            
            # Имитируем нажатие кнопки
            QTest.mouseClick(button, Qt.MouseButton.LeftButton)
            QApplication.processEvents()
            
            # Проверяем вызов
            mock_method.assert_called_once()
    
    def test_button_properties(self):
        """Тест свойств кнопки"""
        window = MainWindow()
        self.assertEqual(window.button.text(), "select image")
        self.assertEqual(window.button.width(), 150)
        self.assertEqual(window.button.height(), 170)
        window.close()
    
    def test_button_styles(self):
        """Тест стилей кнопки"""
        window = MainWindow()
        style = window.button.styleSheet()
        self.assertIn("background-color: #7f7f7f", style)
        self.assertIn("border-radius: 5px", style)
        window.close()

if __name__ == "__main__":
    unittest.main()