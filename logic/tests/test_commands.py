# logic/tests/test_commands
from abc import ABC
from unittest import TestCase
import unittest

from logic.commands import Command, ConvertImageCommand
from logic.converters import SimpleConversionStrategy


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

    def test_abstract_command_class_has_undo_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода undo
        '''
        self.assertTrue(
            hasattr(Command, 'undo'),
            'Метода undo не существует для Command'
            )
        self.assertTrue(
            callable(getattr(Command, 'undo')),
            f'Не инициализрован метод undo для {self.interface_name}'
        )

    def test_undo_method_is_abstract(self):
        '''
        Тест: Command имеет декоратор abstractmethod для метода undo
        '''
        undo_method = getattr(Command, 'undo')
        self.assertTrue(
            getattr(undo_method, '__isabstractmethod__', False),
             "Метод undo должен быть помечен как @abstractmethod"
             )
        

class ConreteCommandClassesTest(TestCase):
    def setUp(self):
        self.convert_image_cmd = ConvertImageCommand
        self.strategy_sim = SimpleConversionStrategy()
        
    def test_convert_image_command(self):
        '''Тест: Реализация метода execute в конкретной команде'''
        execute_method = getattr(self.convert_image_cmd, 'execute')
        self.assertFalse(getattr(execute_method, '__isabstractmethod__', False))
        
    def test_undo_image_command(self):
        '''Тест: Реализация метода undo в конкретной команде'''
        undo_method = getattr(self.convert_image_cmd, 'undo')
        self.assertFalse(getattr(undo_method, '__isabstractmethod__', False))

    def test_execute_command(self):
        '''Тест: Корректность работы execute-метода'''
        file = 'dog.webp'
        command = ConvertImageCommand(self.strategy_sim, file)
        command.execute()
        self.assertEqual(command._out_file, f'Simple conversion for {file}...', 
                         'Файл не конвертируется по команде execute')

    def test_undo_command(self):
        '''Тест: Корректность работы undo-метода'''
        file = 'dog.webp'
        command = ConvertImageCommand(self.strategy_sim, file)
        command.execute()
        command.undo()
        self.assertIsNone(command._out_file, 'Undo-команда не должна оставлять файла на экспорт')


if __name__ == "__main__":
    unittest.main()