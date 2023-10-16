class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        pair = defaultdict(int)

        for n in nums:
            if pair[n]:
                res += 1
                pair[n] -=1 
            else:
                pair[k-n] += 1
        
        return res

