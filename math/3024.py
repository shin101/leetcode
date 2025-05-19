class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 2:
            if sum(nums[0:2]) > nums[2]:
                return "isosceles"
            else:
                return "none"
        elif len(set(nums)) == 3:
            if sum(nums[0:2]) > nums[2]:
                return "scalene"
            else:
                return "none"