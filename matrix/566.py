class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[0 for _ in range(c)] for _ in range(r)]

        if r*c!=rows*cols:
            return mat
        
        temp = []

        for i in range(rows):
            for j in range(cols):
                temp.append(mat[i][j])
        print(res)
        print(temp)

        cnt = 0
        for i in range(r):
            for j in range(c):
                print(temp[cnt])
                res[i][j] = temp[cnt]
                cnt +=1
        
        return res
