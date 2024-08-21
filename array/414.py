class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = set(nums)
        unique_sorted = sorted(unique, reverse=True)

        if len(unique_sorted)>2:
            return unique_sorted[2]
        
        return unique_sorted[0]
