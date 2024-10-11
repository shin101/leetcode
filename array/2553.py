class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        for idx, num in enumerate(nums):
            nums[idx] = list(str(num))

        
        return([int(n) for num in nums for n in num])
        
