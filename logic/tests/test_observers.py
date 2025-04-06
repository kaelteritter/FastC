# logic/tests/test_Subjects
from abc import ABC
from unittest import TestCase

from logic.observers import Subject


class SubjectInterfaceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.interface_name = 'Базовый класс для Уведомлений (Subject)'
        return super().setUpClass()
    
    def test_subject_interface_has_docs(self):
        self.assertIsNotNone(
            Subject.__doc__, 
            f'Нет документации для {self.interface_name}'
                             )
    
    def test_abstract_subject_interface_exists(self):
        '''
        Тест: Существование базового интерфейса команд
        '''
        try: 
            from logic.observers import Subject
            self.assertTrue(Subject)
        except (ModuleNotFoundError, ImportError):
            self.fail(f'Не существует: {self.interface_name}')

    def test_subject_class_is_abstract(self):
        '''
        Тест: Класс команды наследуется от ABC
        '''
        self.assertTrue(issubclass(Subject, ABC), f'{self.interface_name} не наследуется от ABC')

    def test_abstract_subject_class_has_attach_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода attach
        '''
        self.assertTrue(
            hasattr(Subject, 'attach'),
            'Метода attach не существует для Subject'
            )
        self.assertTrue(
            callable(getattr(Subject, 'attach')),
            f'Не инициализрован метод attach для {self.interface_name}'
        )

    def test_attach_method_is_abstract(self):
        '''
        Тест: Subject имеет декоратор abstractmethod для метода attach
        '''
        attach_method = getattr(Subject, 'attach')
        self.assertTrue(
            getattr(attach_method, '__isabstractmethod__', False),
             "Метод attach должен быть помечен как @abstractmethod"
             )