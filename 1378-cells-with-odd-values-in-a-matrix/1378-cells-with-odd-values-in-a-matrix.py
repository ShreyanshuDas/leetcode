class Solution:
    def oddCells(self, m, n, indices):
        row_counts = [0] * m
        col_counts = [0] * n
        
        for ri, ci in indices:
            row_counts[ri] += 1
            col_counts[ci] += 1
        
        odd_count = 0
        for i in range(m):
            for j in range(n):
                if (row_counts[i] + col_counts[j]) % 2 != 0:
                    odd_count += 1
        return odd_count