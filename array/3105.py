class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        curr = 1
        increasing = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if increasing == -1:
                    curr +=1
                else:
                    increasing = -1
                    curr = 2
            elif nums[i] < nums[i+1]:
                if increasing == 1:
                    curr +=1
                else:
                    increasing = 1
                    curr = 2
            else:
                curr = 1
                increasing =0

            res = max(res, curr)
        return res