from abc import ABC, abstractmethod


class ConversionStrategy(ABC):
    '''Базовый класс стратегии конвертации'''
    @abstractmethod
    def convert(self):
        pass
