

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        max_sum = curr_sum = sum(nums[:k])

        # if len(nums) == 1 :
        #     return nums[0]

        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum/k

