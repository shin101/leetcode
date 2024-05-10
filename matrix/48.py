class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose

        for r in range(len(matrix)): # ?? check later
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        for row in matrix:
            row = row.reverse()
        
        return matrix
