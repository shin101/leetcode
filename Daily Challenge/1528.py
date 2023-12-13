class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        counter = 0
        rows = len(mat)
        cols = len(mat[0])
        rowSum = [0] * rows
        colSum = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 :
                    rowSum[r] += 1 
                    colSum[c] += 1

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and rowSum[r] == 1 and colSum[c] == 1 :
                    counter += 1 

        return counter

