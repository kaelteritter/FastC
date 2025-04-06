from abc import ABC, abstractmethod


class Command(ABC):
    '''Базовый класс команд'''
    @abstractmethod
    def execute(self):
        pass