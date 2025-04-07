from .converters import AdvancedConversionStrategy, SimpleConversionStrategy


class FileConverterFactory:
    def __init__(self):
        self.converters = {
            "simple": SimpleConversionStrategy,
            "advanced": AdvancedConversionStrategy,
        }

    def create_converter(self, conversion_type: str):
        if not conversion_type in self.converters:
            raise ValueError('Неверный тип конверсии')
        return self.converters[conversion_type]()
    

    # AssertionError: <class 'logic.converters.SimpleConversionStrategy'> 
    # is not an instance of <class 'logic.converters.SimpleConversionStrategy'>