class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0

        while len(nums)>0:
            if len(set(nums))==len(nums):
                return cnt
            
            cnt+=1
            nums = nums[3:]
        
        return cnt