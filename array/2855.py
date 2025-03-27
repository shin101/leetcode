class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        first = min(nums)
        res = 0

        if sorted(nums)==nums:
            return 0

        for i, num in enumerate(nums):
            if num==first:
                left = nums[:i]
                right = (nums[i:])
                res = len(nums)-i
                break

        return res if right+left == sorted(nums) else -1