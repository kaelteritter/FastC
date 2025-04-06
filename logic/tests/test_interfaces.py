# logic/tests/test_interfaces
from abc import ABC
from unittest import TestCase

from logic.converters import ConversionStrategy


class StrategyInterfaceTest(TestCase):
    def setUp(self):
        self.abstract_strategy = ConversionStrategy()

    def test_abstract_strategy_interface_exists(self):
        '''
        Тест: Существование базового интерфейса стратегии
        '''
        try: 
            from logic.converters import ConversionStrategy
            self.assertTrue(ConversionStrategy)
        except (ModuleNotFoundError, ImportError):
            self.fail('Не существует базового интерфейса для стратегии конвертации')

    def test_strategy_class_is_abstract(self):
        '''
        Тест: Класс стратегии наследуется от ABC
        '''
        self.assertIsInstance(self.abstract_strategy, ABC, 'Класс не наследуется от ABC')

    def test_abstract_strategy_class_has_convert_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода convert
        '''
        self.assertTrue(
            hasattr(self.abstract_strategy, 'convert'),
            'Метода convert не существует для ConversionStrategy'
            )
        self.assertTrue(
            callable(getattr(self.abstract_strategy, 'convert')),
            'Не инициализрован метод convert для базового ConversionStrategy'
        )