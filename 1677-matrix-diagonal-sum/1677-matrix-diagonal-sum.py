class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]  # Primary diagonal
            total += mat[i][n - 1 - i]  # Secondary diagonal
        
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]  # Subtract the center element once if n is odd
        return total

# The following code is for testing purposes and should be included if needed
def main():
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    mat2 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
    mat3 = [[5]]
    
    solution = Solution()
    print(solution.diagonalSum(mat1))  # Output: 25
    print(solution.diagonalSum(mat2))  # Output: 8
    print(solution.diagonalSum(mat3))  # Output: 5

if __name__ == "__main__":
    main()