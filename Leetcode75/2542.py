class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        minHeap = []
        res = 0 
        n1Sum = 0 

        zipped = [(n1, n2) for n1,n2 in zip(nums1,nums2)]
        zipped = sorted(zipped, key=lambda val:val[1], reverse=True)

        for n1, n2 in zipped:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k :
                popped = heapq.heappop(minHeap)
                n1Sum -= popped
            
            if len(minHeap) == k:
                res = max(res, n1Sum * n2) 
        return res 