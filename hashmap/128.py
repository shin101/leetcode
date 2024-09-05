class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i]-1 not in hashset:
                cnt = 0
                while nums[i]+cnt in hashset:
                    cnt += 1
                res = max(res, cnt)


        return res
