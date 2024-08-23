class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        res =0
        for num in nums:
            if num >= k:
                return res
            res+=1
        
        return res