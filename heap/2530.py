class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k>0:
            popped= -heapq.heappop(nums)
            res+=popped
            heapq.heappush(nums, -ceil(popped/3))
            k-=1
        return res
