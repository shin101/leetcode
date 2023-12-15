class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashset = set()
        for path in paths:
            hashset.add(path[0])
        
        for path in paths:
            if path[1] not in hashset:
                return path[1]