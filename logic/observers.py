from abc import ABC, abstractmethod


class Subject(ABC):
    '''
    Базовый класс Уведомителя
    '''
    @abstractmethod
    def attach(self):
        pass