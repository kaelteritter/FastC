import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest

from gui.main_window import MainWindow

class TestWindowTitle(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Инициализация QApplication
    
    def test_window_title(self):
        window = MainWindow()
        self.assertEqual(window.windowTitle(), "FastC")

if __name__ == "__main__":
    unittest.main()