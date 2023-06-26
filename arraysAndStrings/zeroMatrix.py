''' Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to 0

input = [[1,2, 4], [3, 4, 5], [6, 4, 7]] 
output = [[1,2, 4], [3, 4, 5], [6, 4, 7]] 

input = [[1,2, 4], [3, 4, 5], [6, 0, 7]] 
output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''
def zeroMatrix(matrix):
    count = 0
    while count < len(matrix):
        if 0 in matrix[count]:
            matrix = [[0] *len(matrix[count]) for i in matrix]
        count += 1
    return matrix

matrix = [[1,2, 4], [3, 4, 5], [6, 4, 7]]  
matrix1 = [[1,2, 4], [3, 4, 5], [6, 0, 7]]  
print(zeroMatrix(matrix))
print(zeroMatrix(matrix1))
