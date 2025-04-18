class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = max(questions[i][0] + dfs(i+1+questions[i][1]),
            dfs(i+1))

            return dp[i]

        return dfs(0)