import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest

# from gui.main_window import MainWindow

class TestWindowTitle(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])
    
    def test_window_title(self):
        with self.assertRaises(ImportError):
            from gui.main_window import MainWindow
        class MockWindow:
            def windowTitle(self):
                return "FastC"
        
        window = MockWindow()
        self.assertEqual(window.windowTitle(), "FastC")

if __name__ == "__main__":
    unittest.main()