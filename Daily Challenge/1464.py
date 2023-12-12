class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        s = sorted(nums)
        biggest = s[-1]
        second_biggest = s[-2]

        return (biggest-1) * (second_biggest-1)

        