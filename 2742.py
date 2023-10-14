class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dp(idx, remaining):
            if remaining <= 0:
                return 0
            if idx == len(cost):
                return inf

            paint =  cost[idx] + dp(idx+1, remaining - 1 - time[idx])
            skip = dp(idx+1, remaining)
            
            return min(paint,skip)

        return dp(0, len(cost))



