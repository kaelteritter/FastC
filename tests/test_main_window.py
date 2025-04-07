import unittest

from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import QSize

from gui.main_window import MainWindow

class TestWindowTitle(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Инициализация QApplication
    
    def test_window_title(self):
        """Тест заголовка главного окна"""
        window = MainWindow()
        self.assertEqual(window.windowTitle(), "FastC")

    def test_window_fixed_size(self):
        """Тест фиксированного размера окна"""
        # Ожидаемые размеры
        expected_width = 300
        expected_height = 400
        
        window = MainWindow()
        
        # Проверяем, что размеры фиксированные
        self.assertTrue(window.minimumSize() == window.maximumSize())
        
        # Проверяем точные размеры
        self.assertEqual(window.width(), expected_width)
        self.assertEqual(window.height(), expected_height)
        
        # Альтернативная проверка через size()
        self.assertEqual(window.size(), QSize(expected_width, expected_height))
if __name__ == "__main__":
    unittest.main()