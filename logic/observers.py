from abc import ABC, abstractmethod


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