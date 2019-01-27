"""
Задача: реализовать класс и метод класса для чтения и вывода текста из файла example.txt.
Класс должен работать следующим образом:
reader = FileReader("example.txt")
print(reader.read())

Если файла нет - должен прехватить ошбку IOError и вернуть пустую строку "".

"""


class FileReader:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def read(self):
        try:
            f = open(self.file_path, "r")
            return f.read()
        except IOError:
            return ""
