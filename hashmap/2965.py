class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        cnt = defaultdict(int)
        double, missing = 0,0 

        for i in range(N):
            for j in range(N):
                cnt[grid[i][j]] += 1
                if cnt[grid[i][j]] == 2:
                    double = grid[i][j]
    

        for num in range(1, N*N+1):
            if num not in cnt:
                missing = num
    
        print(cnt)

        return [double, missing]
