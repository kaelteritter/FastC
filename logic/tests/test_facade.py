from tempfile import NamedTemporaryFile
from unittest import TestCase
import unittest

from PIL import Image

from logic.facade import Converter


# class FacadeConverterTest(TestCase):
#     def setUp(self):
#         with NamedTemporaryFile(suffix='.webp', delete=False) as temp_webp:
#             webp_file = temp_webp.name
#             img = Image.new('RGB', (100, 100), color='red')
#             img.save(webp_file, 'WEBP')
#             self.img_webp = webp_file
#         self.main_converter = Converter()

#     def test_facade_converter_converts_webp_to_jpg(self):
#         '''
#         Тест: Фасад-конвертер работает как функтор
#         и конвертирует файлы из WEBP в JPG
#         '''
#         output_file = self.main_converter.convert(self.img_webp, 'webp', 'jpg')
#         print(output_file)
#         self.assertIsNotNone(output_file)
#         self.assertNotEqual(self.img_webp, output_file)


if __name__ == "__main__":
    unittest.main()