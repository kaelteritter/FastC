# logic/tests/test_interfaces
from unittest import TestCase


class StrategyInterfaceTest(TestCase):
    def test_abstract_strategy_interface_exists(self):
        try: 
            from logic.converters import ConversionStrategy
            self.assertTrue(True)
        except (ModuleNotFoundError, ImportError):
            self.fail('Не существует базового интерфейса для стратегии конвертации')

    def test_abstract_strategy_class_has_convert_method(self):
        ...