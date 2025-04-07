from abc import ABC, abstractmethod

from .observers import ConversionNotifier

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
    def __init__(
            self, 
            strategy: ConversionStrategy,
            notifier: ConversionNotifier,
            _in_file
                 ):
        self.strategy = strategy
        self.notifier = notifier
        self._in_file = _in_file
        self._out_file = None

    def execute(self):
        self._out_file = self.strategy.convert(self._in_file)
        self.notifier.notify(f"Conversion completed for {self._out_file}")
        return self._out_file

    def undo(self):
        if self._out_file is not None:
            self.notifier.notify(f"Conversion undone for {self._out_file}")
            self._out_file = None