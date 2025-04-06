from abc import ABC, abstractmethod


class ConversionStrategy(ABC):
    @abstractmethod
    def convert(self):
        pass
