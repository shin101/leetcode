class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r : 
            mid = (l+r) // 2
            total = 0 

            for num in piles:
                total += math.ceil(num/mid)
            if total > h :
                l = mid + 1
            else:
                res = min(r, mid)
                r = mid - 1
        return res