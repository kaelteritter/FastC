from abc import ABC, abstractmethod
import logging


class Subject(ABC):
    '''
    Базовый класс Уведомителя
    '''
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class Observer(ABC):
    '''
    Базовый класс Наблюдателя
    '''
    @abstractmethod
    def update(self, message):
        pass


class ConversionNotifier(Subject):
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class ConsoleLogger(Observer):
    def __init__(self):
        self.logger = logging.getLogger("ConsoleLogger")
        self.logger.setLevel('INFO')

    def update(self, message):
        self.logger.info(f'[Console Logger] {message}')