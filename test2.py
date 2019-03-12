matrix = [1, 2, None, None, None, None, None, None, None]
size = int(len(matrix) ** 0.5)

print(size)


print("size-1 = ", size)
matrix = [x for x in matrix if x is not None]
matrix.extend([None, ] * ((size - 1) ** 2 - len(matrix)))

print(matrix)


"""
result = ''
        size = int(len(self.matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i) for i in self.matrix[size * row:size * (row + 1)]]) + '\n'
        return result
"""