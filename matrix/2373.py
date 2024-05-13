class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        res = [[0] * (n) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        res[i][j] = max(res[i][j], grid[r][c])

        return res