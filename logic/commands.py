from abc import ABC, abstractmethod


class Command(ABC):
    '''Базовый класс команд'''
    @abstractmethod
    def execute(self):
        '''Начать конвертацию'''
        pass

    @abstractmethod
    def undo(self):
        '''Отмена конвертации'''
        pass

class ConvertImageCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass