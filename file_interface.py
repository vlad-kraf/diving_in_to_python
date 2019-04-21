import tempfile
import os

class File:
    def __init__(self, path, content = None):
        self.path = path
        self.content = content.split('\n')
        with open(self.path, 'w'):
            pass

    def write(self, content):
        self.content = content
        with open(self.path, 'w') as fp:
            fp.write(self.content)

    def read(self):
        with open(self.path, 'r') as fp:
            output = fp.read()
        return (output)

    def __add__(self, second):
        """В этом случае создается новый файл и файловый объект, в котором содержимое
        второго файла добавляется к содержимому первого файла. Новый файл должен
        создаваться в директории, полученной с помощью tempfile.gettempdir.
        Для получения нового пути можно использовать os.path.join."""

        new_path = os.path.join(tempfile.gettempdir(), 'merge_files.txt')
        content = self.read() + second.read()

        with open(new_path, 'w') as fp:
            fp.write(content)

        return File(new_path)


    def __str__(self):
        """с помощью функции print должен печататься его полный путь, переданный при
        инициализации."""
        return self.path
