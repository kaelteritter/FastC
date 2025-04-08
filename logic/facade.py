# class Converter:
#     def __init__(self):
#         self._in_file

#     def convert_image(self, )
        
#     def __call__(self, file_to_convert: str):
#         return self.convert_image()




from logic.commands import ConvertImageCommand


class Converter:
    def __init__(self, **kwargs):
        # Здесь будет пополняться словарь для будущего расширения
        # работы с разными форматами
        # Пока работаем только с одним
        self.file_formats = {
            'webp': ConvertImageCommand
        }

    def __get_command(self, format_in):
        # Забираем класс команды сообразно типу загруженного файла
        return self.file_formats.get(format_in)

    def convert(self, file, format_in, format_out):
        # Получаем команду и делаем конвертацию
        cmd = self.__get_command(format_in)
        cmd = cmd(file=file, format_in=format_in, format_out=format_out)
        output = cmd.execute()
        return output

    def cancel(self):
        # Если есть запущенные процессы конвертации:
        # Отмена конвертации и удаление мусора
        pass