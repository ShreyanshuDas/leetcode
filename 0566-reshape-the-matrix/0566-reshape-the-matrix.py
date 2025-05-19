class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0
        if m * n != r * c:
            return mat
        
        flattened = []
        for row in mat:
            flattened.extend(row)
        
        reshaped = []
        index = 0
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(flattened[index])
                index += 1
            reshaped.append(new_row)
        
        return reshaped