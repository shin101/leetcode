from typing import List
import heapq

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# hint
# use minheap. set an array and you heapify it
# 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0 :
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res


sol = Solution()
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2)) # [[3,3],[-2,4]]