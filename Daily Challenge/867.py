class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        for i in range(len(matrix[0])):
            inner = []
            for j in range(len(matrix)):
                inner.append(matrix[j][i])
            
            arr.append(inner)

        return arr