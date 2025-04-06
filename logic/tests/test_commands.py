# logic/tests/test_commands
from abc import ABC
from unittest import TestCase

from logic.commands import Command


class CommandInterfaceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.interface_name = 'Базовый класс для интерфейса команд'
        return super().setUpClass()
    
    def test_command_interface_has_docs(self):
        self.assertIsNotNone(
            Command.__doc__, 
            f'Нет документации для {self.interface_name}'
                             )
    
    def test_abstract_command_interface_exists(self):
        '''
        Тест: Существование базового интерфейса команд
        '''
        try: 
            from logic.commands import Command
            self.assertTrue(Command)
        except (ModuleNotFoundError, ImportError):
            self.fail(f'Не существует: {self.interface_name}')

    def test_command_class_is_abstract(self):
        '''
        Тест: Класс команды наследуется от ABC
        '''
        self.assertTrue(issubclass(Command, ABC), f'{self.interface_name} не наследуется от ABC')

    def test_abstract_command_class_has_execute_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода execute
        '''
        self.assertTrue(
            hasattr(Command, 'execute'),
            'Метода execute не существует для Command'
            )
        self.assertTrue(
            callable(getattr(Command, 'execute')),
            f'Не инициализрован метод execute для {self.interface_name}'
        )

    def test_execute_method_is_abstract(self):
        '''
        Тест: Command имеет декоратор abstractmethod для метода execute
        '''
        execute_method = getattr(Command, 'execute')
        self.assertTrue(
            getattr(execute_method, '__isabstractmethod__', False),
             "Метод execute должен быть помечен как @abstractmethod"
             )