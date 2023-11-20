class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 
        c = Counter(nums)
        return max(c, key=lambda key:c[key])