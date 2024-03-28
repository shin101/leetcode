class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        c = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            c[nums[r]] += 1

## {1:1, 4:2, }
            while c[nums[r]] > k:
                c[nums[l]] -= 1
                l+=1
   
            res = max(res, r - l + 1 )


        return res
        