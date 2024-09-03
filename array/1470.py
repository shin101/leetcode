class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = n
        l = 0
        res = []

        while mid < len(nums):
            res.append(nums[l])
            res.append(nums[mid])
            l+=1
            mid+=1
        
        return res