# logic/tests/test_Subjects
from abc import ABC
from unittest import TestCase

from logic.observers import Observer, Subject


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
        
    def test_abstract_subject_class_has_detach_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода detach
        '''
        self.assertTrue(
            hasattr(Subject, 'detach'),
            'Метода detach не существует для Subject'
            )
        self.assertTrue(
            callable(getattr(Subject, 'detach')),
            f'Не инициализрован метод detach для {self.interface_name}'
        )

    def test_detach_method_is_abstract(self):
        '''
        Тест: Subject имеет декоратор abstractmethod для метода detach
        '''
        detach_method = getattr(Subject, 'detach')
        self.assertTrue(
            getattr(detach_method, '__isabstractmethod__', False),
             "Метод detach должен быть помечен как @abstractmethod"
             )
        
    def test_abstract_subject_class_has_notify_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода notify
        '''
        self.assertTrue(
            hasattr(Subject, 'notify'),
            'Метода notify не существует для Subject'
            )
        self.assertTrue(
            callable(getattr(Subject, 'notify')),
            f'Не инициализрован метод notify для {self.interface_name}'
        )

    def test_notify_method_is_abstract(self):
        '''
        Тест: Subject имеет декоратор abstractmethod для метода notify
        '''
        notify_method = getattr(Subject, 'notify')
        self.assertTrue(
            getattr(notify_method, '__isabstractmethod__', False),
             "Метод notify должен быть помечен как @abstractmethod"
             )
        

class ObserverInterfaceTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.interface_name = 'Базовый класс для Уведомлений (Observer)'
        return super().setUpClass()
    
    def test_observer_interface_has_docs(self):
        self.assertIsNotNone(
            Observer.__doc__, 
            f'Нет документации для {self.interface_name}'
                             )
    
    def test_abstract_observer_interface_exists(self):
        '''
        Тест: Существование базового интерфейса команд
        '''
        try: 
            from logic.observers import Observer
            self.assertTrue(Observer)
        except (ModuleNotFoundError, ImportError):
            self.fail(f'Не существует: {self.interface_name}')

    def test_observer_class_is_abstract(self):
        '''
        Тест: Класс команды наследуется от ABC
        '''
        self.assertTrue(issubclass(Observer, ABC), f'{self.interface_name} не наследуется от ABC')

    def test_abstract_observer_class_has_update_method(self):
        '''
        Тест: Проверка инициализации абстрактного метода update
        '''
        self.assertTrue(
            hasattr(Observer, 'update'),
            'Метода update не существует для Observer'
            )
        self.assertTrue(
            callable(getattr(Observer, 'update')),
            f'Не инициализрован метод update для {self.interface_name}'
        )

    def test_update_method_is_abstract(self):
        '''
        Тест: Observer имеет декоратор abstractmethod для метода update
        '''
        update_method = getattr(Observer, 'update')
        self.assertTrue(
            getattr(update_method, '__isabstractmethod__', False),
             "Метод update должен быть помечен как @abstractmethod"
             )
  