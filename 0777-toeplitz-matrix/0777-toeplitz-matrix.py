class Solution:
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
        