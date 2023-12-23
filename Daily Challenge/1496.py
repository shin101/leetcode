class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = (0,0)
        visited = set()
        visited.add(curr)

        for p in path:
            if p == "N":
                curr = (curr[0], curr[1]+1)
            elif p == "S":
                curr = (curr[0], curr[1]-1)
            elif p == "E":
                curr = (curr[0]+1, curr[1])
            else:
                curr = (curr[0]-1, curr[1])
            if curr in visited:
                return True
            visited.add(curr)

        return False
