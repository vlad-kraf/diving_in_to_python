matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for _ in range(8):
    size = int(len(matrix) ** 0.5)
    print("len_m: ", len(matrix))
    print("size: ", size)

    # узнаем индекс последнего "не нулевого" элемента
    if size == 1 and matrix[0] is None:
        idx = 1001
    else:
        for i in matrix:
            if i is not None:
                idx = matrix.index(i)
    print("index: ", idx)


    # запоминаем не нулевой элемент
    result = matrix[idx]
    print("result: ", result)

    # заменяем не нулевой элемент на None
    matrix[idx] = None
    print("matrix + None: ", matrix)



    # проверяем нужно ли уменьшать размер матрицы


    print("matrix_without_none:", matrix)
    idx = idx-1
    print("New_idx", idx)

    if idx < (size * (size - 1)):
        print("<<<<")
        size = size - 1
        matrix = [x for x in matrix if x is not None]
        matrix.extend([None, ] * ((size ** 2) - len(matrix)))

    print("Final: ", matrix)
    print("-------------------------------")