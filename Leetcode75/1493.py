class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = start = zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0 :
                zeros +=1 
            while zeros > 1 :
                if nums[start] == 0:
                    zeros -=1 
                start += 1
            res = max(res, len(nums[start:i+1]))
        return res-1
