class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for num, cnt in c.items():
            if cnt == 1:
                res += num
        
        return res