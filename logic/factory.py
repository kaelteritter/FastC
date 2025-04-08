from .converters import AdvancedConversionStrategy, SimpleConversionStrategy


class FileConverterFactory:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if not self.__class__._initialized:
            self.converters = {
                "simple": SimpleConversionStrategy,
                "advanced": AdvancedConversionStrategy,
            }
            self.__class__._initialized = True

    def create_converter(self, conversion_type: str):
        if not conversion_type in self.converters:
            raise ValueError('Неверный тип конверсии')
        return self.converters[conversion_type]()
    

    # AssertionError: <class 'logic.converters.SimpleConversionStrategy'> 
    # is not an instance of <class 'logic.converters.SimpleConversionStrategy'>