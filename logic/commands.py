from abc import ABC, abstractmethod

from .converters import ConversionStrategy


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
    def __init__(self, 
                 strategy: ConversionStrategy,
                 _in_file):
        self.strategy = strategy
        self._in_file = _in_file
        self._out_file = None

    def execute(self):
        self._out_file = self.strategy.convert(self._in_file)
        return self._out_file

    def undo(self):
        if self._out_file is not None:
            self._out_file = None