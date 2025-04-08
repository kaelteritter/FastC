# logic/tests/test_interfaces
from abc import ABC
import os
from tempfile import NamedTemporaryFile
from unittest import TestCase
import unittest

from PIL import Image
from logic.converters import ConversionStrategy, WebpToJpgStrategy


class StrategyInterfaceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.interface_name = 'Базовый класс для интерфейса стратегии конвертации'
        return super().setUpClass()
    
    def test_abstract_strategy_interface_exists(self):
        '''
        Тест: Существование базового интерфейса стратегии
        '''
        try: 
            from logic.converters import ConversionStrategy
            self.assertTrue(ConversionStrategy)
        except (ModuleNotFoundError, ImportError):
            self.fail('Не существует базового интерфейса для стратегии конвертации')

    def test_strategy_interface_has_docs(self):
        self.assertIsNotNone(
            ConversionStrategy.__doc__, 
            f'Нет документации для {self.interface_name}'
                             )

    def test_strategy_class_is_abstract(self):
        '''
        Тест: Класс стратегии наследуется от ABC
        '''
        self.assertTrue(issubclass(ConversionStrategy, ABC), 'Класс не наследуется от ABC')

    def test_abstract_strategy_class_has_convert_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода convert
        '''
        self.assertTrue(
            hasattr(ConversionStrategy, 'convert'),
            'Метода convert не существует для ConversionStrategy'
            )
        self.assertTrue(
            callable(getattr(ConversionStrategy, 'convert')),
            'Не инициализрован метод convert для базового ConversionStrategy'
        )

    def test_convert_method_is_abstract(self):
        '''
        Тест: ConversionStrategy имеет декоратор abstractmethod для метода convert
        '''
        convert_method = getattr(ConversionStrategy, 'convert')
        self.assertTrue(
            getattr(convert_method, '__isabstractmethod__', False),
             "Метод convert должен быть помечен как @abstractmethod"
             )
        
    

class WebpToJpgStrategyTest(TestCase):
    def test_webp_to_jpg_strategy_converting_files_correctly(self):
        with NamedTemporaryFile(suffix='.webp', delete=False) as temp_webp:
            webp_file = temp_webp.name
            img = Image.new('RGB', (100, 100), color='red')
            img.save(webp_file, 'WEBP')

        with NamedTemporaryFile(suffix='.jpg', delete=False) as temp_jpg:
            jpg_file = temp_jpg.name

        try:
            strategy = WebpToJpgStrategy()
            strategy.convert(webp_file, jpg_file)

            self.assertTrue(os.path.exists(jpg_file), 'Файл не был сконвертирован')

            with Image.open(jpg_file) as img:
                self.assertEqual(img.format, 'JPEG')
                self.assertEqual(img.size, (100, 100))
                self.assertEqual(img.mode, 'RGB')
        finally:
            os.unlink(webp_file)
            os.unlink(jpg_file)







if __name__ == "__main__":
    unittest.main()