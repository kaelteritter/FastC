# logic/tests/test_commands
from unittest import TestCase

from logic.commands import Command


class CommandInterfaceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.interface_name = 'Базовый класс для интерфейса команд'
        return super().setUpClass()
    
    def test_strategy_interface_has_docs(self):
        self.assertIsNotNone(
            Command.__doc__, 
            f'Нет документации для {self.interface_name}'
                             )
    
    def test_abstract_strategy_interface_exists(self):
        '''
        Тест: Существование базового интерфейса команд
        '''
        try: 
            from logic.commands import Command
            self.assertTrue(Command)
        except (ModuleNotFoundError, ImportError):
            self.fail(f'Не существует: {self.interface_name}')
