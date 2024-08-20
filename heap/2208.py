class Solution:
    def halveArray(self, nums: List[int]) -> int:
        res = 0
        total = sum(nums)
        half = total/2
        nums = [-num for num in nums]

        heapq.heapify(nums)
   
        while half > 0:
            popped = heapq.heappop(nums) / 2
            half += popped
            heapq.heappush(nums,popped)
            res+=1

        return res
