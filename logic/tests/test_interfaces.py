# logic/tests/test_interfaces
from abc import ABC
from unittest import TestCase
import unittest
from logic.converters import AdvancedConversionStrategy, ConversionStrategy, SimpleConversionStrategy


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
        
    
class StrategyConreteClassesTest(TestCase):
    def setUp(self):
        self.simple = SimpleConversionStrategy.__name__
        self.advanced = AdvancedConversionStrategy.__name__
        self.simple_strategy = SimpleConversionStrategy()
        self.advanced_strategy = AdvancedConversionStrategy()

    def test_conrete_strategy_has_convert_method_realized(self):
        '''
        Тест: SimpleConversionStrategy, AdvancedConversionStrategy 
        реализуют метод convert
        '''
        convert_method = getattr(SimpleConversionStrategy, 'convert')
        self.assertFalse(
            getattr(convert_method, '__isabstractmethod__', False),
             f"Метод convert должен быть имплементирован в {self.simple}"
             )
        convert_method = getattr(AdvancedConversionStrategy, 'convert')
        self.assertFalse(
            getattr(convert_method, '__isabstractmethod__', False),
             f"Метод convert должен быть имплементирован в {self.advanced}"
             )
        
    def test_simple_strategy_convert_method_work(self):
        file = 'example.webp'
        conversion_simple = self.simple_strategy.convert(file)
        conversion_advanced = self.advanced_strategy.convert(file)

        self.assertEqual(conversion_simple, f'Simple conversion for {file}...')
        self.assertEqual(conversion_advanced, f'Advanced conversion for {file}...')












if __name__ == "__main__":
    unittest.main()