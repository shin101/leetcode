class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        missing = (mean * (len(rolls)+n)) - sum_rolls

        if missing < n or missing > 6 * n:
            return []
        
        remaining_mean = missing // n
        mod = missing % n

        res = [remaining_mean] * n

        for i in range(mod):
            res[i]+=1
    
        return res
        

        