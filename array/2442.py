class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        flipped = [0]*len(nums)

        for i in range(len(nums)):
            flipped[i] = int(str(nums[i])[::-1])

        return len(set(flipped + nums))