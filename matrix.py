def create_matrix(size):
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное 0).
    :param size: int > 0
    :return: list
    """

    matrix = []
    if size > 0 and type(size) == int:
        matrix = [[None] * size for _ in range(size)]

    return matrix


def find_row_with_zerow(matrix):
    """
    Функция принимает на вход двумерный список(матрицу), ищет и возвращает индекс вложенного массива
    (номер строки матрицы) и индекс элемента во вложенном массиме для первого найденного элемента None
    """

    zero_index = [(x, y) for x in range(len(matrix)) for y in range(len(matrix)) if matrix[x][y] is None]

    return zero_index[0]


def len_matrix(matrix):
    """
    Функция принимает на вход двумерный список(матрицу) и возвращает количество всех элементов матрицы
    """
    summ = 0
    for i in matrix:
        summ = summ + len(i)
    return summ


def create_flat_matrix(matrix):
    """
    Функция принимает на вход двумерный список(матрицу) и возвращает одномерный список
    """
    result = []
    for i in matrix:
        result = result + i
    return result


def create_zerous_tail(need_to_add):
    """
    Функция принимает длинну хвоста, и создает одномерный массив из None нужной длинны
    """
    result = [None] * need_to_add
    return result


def new_matrix(matrix, size):
    """
    Функция принимает на вход одномерный массив, size матрицы, и создает двумерных массив размером size х size
    """

    result = []
    k = 0
    for i in range(size):
        result.append([])
        for j in range(size):
            result[i].append(matrix[k])
            k += 1

    return result


def add_element(element, matrix):
    """
    Функция добавляет element в матрицу matrix и при необходимости изменяет размер
    матрицы. Возвращает полученную матрицу.
    :param element: row
    :param matrix: list
    :return: list
    """
    if element is not None:
        row = find_row_with_zerow(matrix)  # индекс строки матрицы содержащий первый элемент None в матрице
        if row[0] == len(matrix) - 1:

            count = ((len(matrix) + 1) * (len(matrix) + 1))  # расчет числа элементов в новой матрице
            new_size = len(matrix) + 1  # расчет нового значения size, для увеличенной матрицы

            flat_matrix = create_flat_matrix(matrix)  # делаем из матрицы одномерный массив

            fact = len(flat_matrix)  # число всех элементов в исходной матрице

            need_to_add = count - fact  # сколько надо добавить нулей

            zerous_tail = create_zerous_tail(need_to_add)  # делаем недостающий хвост из нулей

            matrix = flat_matrix + zerous_tail  # собираем значения + нули в один плоский массив

            matrix = new_matrix(matrix, new_size)  # делаем многомерный массив из одномерного

            item = find_row_with_zerow(matrix)  # находим индекс None который разрешено заменить

            matrix[item[0]][item[1]] = element  # Заменяем None на значение element
        else:
            item = find_row_with_zerow(matrix)  # находим индекс None который разрешено заменить

            matrix[item[0]][item[1]] = element  # Заменяем None на значение element

    return matrix


def matrix_to_string(matrix):
    """
    Функция создает строковое представление matrix - строку, в которой строки матрицы
    разделены переносом строки, а элементы строки разделены пробелами.
    :param matrix: list
    :return: string
    """

    string = ''
    if type(matrix) == list:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if matrix[row][item] is None:
                    string = string + str(matrix[row][item])
                    if item != len(matrix[row])-1:
                        string = string + ' '
                else:
                    string = string + str(matrix[row][item])
                    if item != len(matrix[row])-1:
                        string = string + ' '
            string = string + '\n'

    return str(string)
