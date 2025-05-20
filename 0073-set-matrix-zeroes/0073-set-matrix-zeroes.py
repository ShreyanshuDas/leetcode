class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Check if first row has any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Check if first column has any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # Use first row and column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out marked rows and columns
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0