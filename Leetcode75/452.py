class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        prevEnd = points[0][1]
        total = 1

        for start, end in points[1:]:
            if start > prevEnd :
                prevEnd = end
                total += 1
            else:
                prevEnd = min(end, prevEnd)
        return total
