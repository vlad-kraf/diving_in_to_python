class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        self.max_size = max_size

        if max_size is None:
            self.matrix = [None for _ in range(1 * 1)]
        elif max_size <= Matrix.MAX_SIZE:
            self.matrix = [None for _ in range(max_size * max_size)]
        else:
            self.matrix = [None for _ in range(Matrix.MAX_SIZE * Matrix.MAX_SIZE)]

    def __str__(self):
        """магический метод" _str_ возвращающий строковое представление матрицы - строку,
        в которой строки матрицы разделены переносом строки, а элементы строки разделены пробелами,
        необходим для вывода матрицы на печать.
        """
        result = ''
        size = int(len(self.matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i) for i in self.matrix[size * row:size * (row + 1)]]) + '\n'
        return result
