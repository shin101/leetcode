class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minsum = 1
        maxsum = 1
        for n in nums:
                temp = maxsum * n

                maxsum = max(maxsum * n , minsum * n,  n)
                minsum = min(temp , minsum * n,  n)
                res = max(res, maxsum)

        return res

