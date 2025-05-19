class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        transposed = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed