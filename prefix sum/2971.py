class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = -1
        total = 0
        nums.sort()

        for num in nums:
            if total > num :
                res = num + total

            total += num

        return res

