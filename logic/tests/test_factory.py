import unittest
from unittest import TestCase

from logic.converters import SimpleConversionStrategy
from logic.factory import FileConverterFactory


class FileConverterFactoryTest(TestCase):
    def setUp(self):
        self.factory = FileConverterFactory()
    
    def test_create_simple_converter(self):
        converter = self.factory.create_converter('simple')
        self.assertIsInstance(converter, SimpleConversionStrategy, 
                              'Фабрика не создает конвертер')



if __name__ == "__main__":
    unittest.main()