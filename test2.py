import numpy as np

#создаем массив
size = 4
matrix = np.zeros((size,size), dtype=int)
print(matrix)


#преобразуем массив в строку, 0 заменяем на None
string = ''
for row in range(len(matrix)):
    for item in range(len(matrix[row])):
        if matrix[row][item] == 0:
            string = string + 'None' + ' '
        else:
            string = string + str(matrix[row][item]) + ' '
    string = string + '\n'
print(string)

# заменяем 0 в массиве на значение.
element = 4
for row in range(len(matrix)):
    for item in range(len(matrix[row])):
        if matrix[row][item] == 0:
            matrix[row][item] = element
print(matrix)

# делаем плоский массив из многомерного
matrix = matrix.flatten()
print(matrix)

# делаем массив с количеством элементов равным количеству с добавленной колонкой и строкой
count = 25 #число элементов в массиве где колонки уже добавлены
fact = len(matrix)
need_to_add = count - fact

matrix2 = np.zeros(need_to_add, dtype=int) #делаем недостающий хвост из нулей

matrix = np.concatenate((matrix, matrix2), axis=None)#собираем значения + нули в один плоский массив
print(matrix)

matrix = matrix.reshape((5, 5))#делаем многомерный массив из одномерного
print(matrix)


i,j = np.where(matrix == 0)
print(i[0],j[0])

f = matrix.shape
print (f[0])