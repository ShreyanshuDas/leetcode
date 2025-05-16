class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] 
            total += mat[i][n - 1 - i]  
        
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]  
        return total

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
    print(solution.diagonalSum(mat1))  
    print(solution.diagonalSum(mat2)) 
    print(solution.diagonalSum(mat3))  

if __name__ == "__main__":
    main()