def matrix_manipulation(matrix):
    matrix[0][2] = 0
    return matrix

matrix_inp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_inp)
result = matrix_manipulation(matrix_inp)
print(result)
print(matrix_inp)