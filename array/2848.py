class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        visited = set()

        for start, end in nums:
            visited.update(range(start,end+1))
        
        return len(visited)


           