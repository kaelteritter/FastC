from abc import ABC, abstractmethod

from logic.factory import FileConverterFactory

from logic.observers import ConversionNotifier



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
            converter_type: str,
            notifier: ConversionNotifier,
            _in_file
                 ):
        self.strategy = FileConverterFactory().create_converter(converter_type)
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