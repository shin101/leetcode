class Solution:
    def findKthLargest(self, nums, k) -> int:
        minHeap = [-num for num in nums]
        heapq.heapify(minHeap)

        for i in range(k-1):
            heapq.heappop(minHeap)

        return -heapq.heappop(minHeap)
