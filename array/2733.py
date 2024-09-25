class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        smallest = min(nums)
        biggest = max(nums)

        for num in nums:
            if num!=smallest and num!=biggest:
                return num
        
        return -1