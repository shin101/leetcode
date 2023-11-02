
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums) # 20
        left = 0

        for i, num in enumerate(nums):
            right -= num
            if right == left:
                return i
            else:
                left+= num
        return -1


