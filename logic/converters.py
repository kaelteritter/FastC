from abc import ABC, abstractmethod


class ConversionStrategy(ABC):
    '''Базовый класс стратегии конвертации'''
    @abstractmethod
    def convert(self):
        pass


class SimpleConversionStrategy(ConversionStrategy):
    def convert(self, file):
        return f'Simple conversion for {file}...'


class AdvancedConversionStrategy(ConversionStrategy):
    def convert(self, file):
        return f'Advanced conversion for {file}...'
    

