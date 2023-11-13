class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        start = 0 
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0 :
                zeros +=1 
            while zeros > k :
                if nums[start] == 0 :
                    zeros -= 1
                start +=1 

            res = max(res, (i-start)+1)
        return res