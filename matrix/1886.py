class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows = len(mat)
        i = 0

        if mat == target:
            return True

        while i<3:
            for r in range(rows):
                for c in range(r):
                    mat[r][c], mat[c][r] = mat[c][r],mat[r][c] 

            mat.reverse()
            if mat == target:
                return True
            i +=1

        return False
        