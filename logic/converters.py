from abc import ABC, abstractmethod

from PIL import Image


class ConversionStrategy(ABC):
    '''Базовый класс стратегии конвертации'''
    @abstractmethod
    def convert(self):
        pass
    

class WebpToJpgStrategy(ConversionStrategy):
    def convert(self, file, output=None):
        if output is None:
            output = file.rsplit(".", 1)[0] + ".jpg"

        with Image.open(file) as img:
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(output, "JPEG")
        print(f"Converted {file} to {output}")

        return output